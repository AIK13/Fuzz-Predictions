# This is for CPPDepend. Reads CSVs, and calculates estimated performance of fuzzer
# Must either give csv for raw metrics or raw rules violations

import csv

# as before, all the col names in the estimates file must also be in the raw file.
estimatesFileM = 'CPPDependRankedMetrics.csv'
estimatesFileR = 'CPPDependRankedRules.csv'
estimatesFile = ' ' # left blank because I'll set it after user chooses to use M or R
rawFileM = 'SampleRawCPPDM.csv'
rawFileR = 'SampleRawCPPDR.csv' # TODO: create the raw rules file and test items
rawFile = ' '
choice = -1

# take input for raw filename, or use default
# error handling for entering non-numbers and numbers besides 0 or 1. 
while(not(choice == '0' or choice == '1')):
    choice = input("Do you want estimates based on (0) program metrics, or (1) rules violations? Enter 0 or 1: ")
    if(not(choice == '0' or choice == '1')):
        print("Please enter 0 or 1.")

# set estimateFile and rawFile to correct default
if (choice == '1'): # if choice == 1, set estimates and raw file to rules file
    estimatesFile = estimatesFileR
    rawFile = rawFileR
else:
    estimatesFile = estimatesFileM
    rawFile = rawFileM

# get user raw file, or keep default
userFile = input("Enter filename for raw CPPDepend data in CSV format with no commas within values, or leave blank to use sample data: ")
if(userFile != ""):
    rawFile = userFile


# function to read raw vars and returns them as a dict
def readRaw(filename):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            return row
            # TODO: maybe add ability to check multiple programs at a time?
            # this only checks one program (one row) at a time

rawRow = readRaw(rawFile)

# Function that adds together the regression fxn to get estimated performance
# reads through estimates CV and looks through rawRow for cols to multiply and add together
def readEstimates(filename):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        estimateDict = {'AFL':0} # put in AFL as a dummy value. It'll be reset later
        for row in csv_reader:
            #print(row) # test because CSV file saved as UTF-8 adds strange characters that mess up keys
            estimate = 0
            intercept = 0
            try: # try to catch columns not matching
                if(row['Fuzzer'] != ""):
                    intercept = float(row['Intercept'])
                    for col in row:
                        if(row[col] != 'null' and col != 'Fuzzer' and col != 'Intercept'):
                            estimate += (float(rawRow[col]) * float(row[col]))
                    estimate += intercept
                    estimateDict[row['Fuzzer']] = estimate
            except KeyError as err:
                print("\nERROR: Some columns' names do not match between the raw CSV and the estimates CSV.",
                "If the columns seem to match on your end, it could be an encoding issue.",
                "Try resaving your file as just CSV or CSV MS-DOS")
                print("This is the column we tried to access: ", err)
                exit()
        return estimateDict


estimateDict = readEstimates(estimatesFile)
#print(estimateDict)

# Rank estimates from highest performance to lowest
# this will only work in python3.6+
print("\nPredicted performance from best to worst: ")
for fuzzer in sorted(estimateDict, key=estimateDict.get,reverse=True):
    print(fuzzer,estimateDict[fuzzer])