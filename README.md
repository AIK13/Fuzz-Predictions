# Fuzz-Predictions
Given program metrics, predict fuzzer performance.

**Description:

Fuzz predictions is a simple Python script that estimates fuzzing performance of AFL, AFLFast, AFL++, AFL++_MOPT, AFL++_noalloc, AFLSmart, Eclipser, Entropic, Fairfuzz, FastCGS, HonggFuzz, LaFintel, LibFuzzer, and Mopt given raw program metrics from SourceMonitor or CPPDepend.

**Usage:
Run getEstimatesCPPD.py if your raw data came from CPPDepend, or run getEstimatesSM.py if your raw data came from SourceMonitor.

Raw data should follow the same column names as in the sample CSV files bloatyRawCPPDM.csv, bloatyRawCPPDR.csv, and bloatyRawSM.csv. 

The estimates CSV files, CPPDependRankedMetrics.csv, CPPDependRankedRules.csv, and SourceMonitorRanked.csv, should not be edited unless you want to update the regression function.

The estimates CSV files contain the intercept and estimates values found when creating a stepwise regression function using raw data and fuzzer performance found here https://www.fuzzbench.com/reports/.

The report from 4/1/2020 was used for performance data. A copy of that data is found here https://docs.google.com/spreadsheets/d/1BLeZFTdqhVcWOTcxzTNQbvIuJzj8q6cHtp7Zn4-DWK0/edit?usp=sharing .

**Recommended usage:
Currently, getEstimatesCPPD.py gives the best predictions when using program metrics.
