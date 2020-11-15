# This is for SourceMonitor. Reads CSVs of raw data and gets performance estimates for all the fuzzers tested
# heavily used https://realpython.com/python-csv/ for csv reading code
import csv
estimatesFile = 'SourceMonitorRanked.csv'
rawFile = 'SampleRawSM.csv'

# take input for raw filename... or use default file
userFile = input("Enter filename for raw SourceMonitor data in CSV format with no commas within values, or leave blank to use sample data: ")
if(userFile != ""):
    rawFile = userFile

# function to read the raw vars returns them as a dict
# I am assuming the col names are the same as in the estimate csv below
# The col names HAVE TO match the col names in estimates csv. 
#I'm assuming the user tables are going to be well formatted. Bold assumption, I know.
def readRaw(filename):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader: # there should only be 1 row. I'm assuming user only want to check 1 program
            # TODO: maybe add ability to check multiple programs at a time?
            #print(row) # test
            return row

rawRow = readRaw(rawFile)

# function that adds together the regression function to get an estimated performance
# also reads through the R results csv 
# ESTIMATES CSV MUST PRESENT COLS IN ORDER OF Fuzzer, Intercept, Files, Statements, 
#       Max Complexity, Avg Complexity, Functions, Max Depth, Avg Depth, % Branches
# yes, I could code in a failsafe for that, but I didn't, because this csv is not given by the user.       
def readEstimates(filename):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #count = 0
        #setting up the estimates dictionary
        estimateDict = {'AFL':0} # put in AFL as a dummy value. It'll be reset later
        for row in csv_reader:
            estimate = 0
            intercept = 0
            try: # try to catch columns not matching
                if(row['Fuzzer'] != ""): # if the first col is not empty; i.e. if row is not empty.
                    #print("GETTING ESTIMATE FOR ", row['Fuzzer'])
                    intercept = float(row['Intercept'])
                    for col in row:
                        #print(row[col]) #test
                        if(row[col] != 'null' and col != 'Fuzzer' and col != 'Intercept'):
                            #print("\n",col)
                            #print("raw row: ", rawRow[col])
                            #print("row: ", row[col])
                            estimate += (float(rawRow[col]) * float(row[col]))
                            #print(estimate)
                    estimate += intercept
                    estimateDict[row['Fuzzer']] = estimate
            except KeyError as err:
                print("\nERROR: Some columns' names do not match between the raw CSV and the estimates CSV.",
                "If the columns seem to match on your end, it could be an encoding issue.",
                "Try resaving your file as just CSV or CSV MS-DOS")
                print("This is the col we tried to access: ", err)
                exit()
        return estimateDict

estimateDict = readEstimates(estimatesFile)


# Rank estimates from highest performance to lowest
# this will only work in python3.6+
# heavily used this https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value 
#estimateDict = ({k: v for k, v in sorted(estimateDict.items(), key=lambda item: item[1],reverse=True)})
#print(estimateDict)

print("\nPredicted performance from best to worst: ")
for fuzzer in sorted(estimateDict, key=estimateDict.get,reverse=True):
    print(fuzzer,",",estimateDict[fuzzer])
    
#TODO: maybe, possibly, add exception handling for if user input is badly formatted
# or if the estimates csv needs a variable that isn't given by the user? 
# I'd need to say something about the prediction being impossible without all the vals