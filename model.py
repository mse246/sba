import csv
import numpy as np
import pandas as pd
import datetime

###################
# Reading in data #
###################
# df = pd.read_csv('SBA_Loan_data_.csv',)

'''
#approval_dates = df.iloc[:]['ApprovalDate']
# months = [datetime.datetime.strptime(x, '%m/%d/%y').date() for x in approval_dates]
# print(months)

test = datetime.datetime.strptime('1990-01', '%Y-%m').date()
print(test)
'''

#####################################################
# TODO Write rules to fill in additional covariates #
#####################################################

'''
Federal Funds Rates
'''
fed_funds_df = pd.read_csv('./covariates_raw/FEDFUNDS.csv')
print(fed_funds_df);print

'''
Savings Rates
'''
savings_rates_df = pd.read_csv('./covariates_raw/SavingsRate.csv')
print(savings_rates_df);print

'''
US Dollar Index
'''
us_dollar_index_df = pd.read_csv('./covariates_raw/us-dollar-index-historical-chart.csv')
print(us_dollar_index_df);print

'''
Housing Prices
'''
housing_prices_df = pd.read_csv('./covariates_raw/Zip_MedianValuePerSqft_AllHomes.csv')
print(housing_prices_df);print

'''
US Import Price Index
'''
us_import_price_index_df = pd.read_csv('./covariates_raw/US_Import_Price_Index.csv')
print(us_import_price_index_df);print

'''
US Uncertainty Index
'''
us_uncertainty_index_df = pd.read_csv('./covariates_raw/US_Uncertainty_Index.csv')
print(us_uncertainty_index_df);print

'''
'''

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
