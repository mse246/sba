import csv
import numpy as np

###################
# Reading in data #
###################
data = []
with open('SBA_Loan_data_.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        data.append(row)

sba_data = np.array(data)

#####################################################
# TODO Write rules to fill in additional covariates #
#####################################################

def fillCountyUnemploymentRate():
    pass

def fillCovariates():
    pass
'''
County Unemployment Rate 
Crisis Indicator Variables 
National Interest Rate 
Employment Diffusion 
Economic Policy Uncertainty Index 
Political State 
Small Business Optimism Index 
National Savings Rate 
Zillow Housing Aspirations 
'''
