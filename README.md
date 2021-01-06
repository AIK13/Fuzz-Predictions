# Fuzz-Predictions
Given program metrics, predict fuzzer performance.

**Description**:

Fuzz predictions is a simple Python script that estimates fuzzing performance of AFL, AFLFast, AFL++, AFL++_MOPT, AFL++_noalloc, AFLSmart, Eclipser, Entropic, Fairfuzz, FastCGS, HonggFuzz, LaFintel, LibFuzzer, and Mopt given raw program metrics from SourceMonitor or CPPDepend.

For the full report and an explanation of the research please see https://github.com/AIK13/Fuzz-Predictions/blob/main/Data/Final%20Report.pdf

**Usage**:
Run getEstimatesCPPD.py if your raw data came from CPPDepend, or run getEstimatesSM.py if your raw data came from SourceMonitor.

Raw data should follow the same column names as in the sample CSV files SampleRawCPPDM.csv, SampleRawCPPDR.csv, and SampleRawSM.csv. 

The estimates CSV files, CPPDependRankedMetrics.csv, CPPDependRankedRules.csv, and SourceMonitorRanked.csv, should not be edited unless you want to update the regression model.

The estimates CSV files contain the intercept and estimates values found when creating a stepwise regression function using raw data and fuzzer performance found here https://www.fuzzbench.com/reports/ and in Fuzz-Predictions/Data/"Fuzzbench Performance data.xlsx".

The report from 4/1/2020 was used for performance data. A copy of that data is found here Fuzz-Predictions/Data/"Fuzzbench Performance data.xlsx".

**Recommended usage**:
Currently, getEstimatesCPPD.py gives the best predictions when using program metrics. Predictions averages for estimates vs real values can also be found in Fuzz-Predictions/Data/"Estimates Vs Real Performance.xlsx"
