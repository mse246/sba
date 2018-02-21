import csv
import numpy as np
import pandas as pd
import datetime

###################
# Reading in data #
###################
df = pd.read_csv('SBA_Loan_data_.csv',)

'''
# approval_dates = df.iloc[:]['ApprovalDate']
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
print('fed_funds_df');print(fed_funds_df);print

'''
Savings Rates
'''
savings_rates_df = pd.read_csv('./covariates_raw/SavingsRate.csv')
print('savings_rates_df'); print(savings_rates_df);print

'''
US Dollar Index
'''
us_dollar_index_df = pd.read_csv('./covariates_raw/us-dollar-index-historical-chart.csv')
print('us_dollar_index_df'); print(us_dollar_index_df);print

'''
Housing Prices
'''
housing_prices_df = pd.read_csv('./covariates_raw/Zip_MedianValuePerSqft_AllHomes.csv')
print('housing_prices_df'); print(housing_prices_df);print

'''
US Import Price Index
'''
us_import_price_index_df = pd.read_csv('./covariates_raw/US_Import_Price_Index.csv')
print('us_import_price_index_df'); print(us_import_price_index_df);print

'''
US Uncertainty Index
'''
us_uncertainty_index_df = pd.read_csv('./covariates_raw/US_Uncertainty_Index.csv')
print('us_uncertainty_index_df'); print(us_uncertainty_index_df);print

'''
Small Business Confidence
'''
sm_business_conf_df = pd.read_csv('./covariates_raw/Small_business_confidence.csv')
print('sm_business_conf_df'); print(sm_business_conf_df);print

'''
Crisis Indicator
'''
crisis_indicator_df = pd.read_csv('./covariates_raw/crisisindicator.csv')
print('crisis_indicator_df'); print(crisis_indicator_df);print

'''
National Unemployement Rate
'''
natl_unemploy_rate_df = pd.read_csv('./covariates_raw/NationalUnemploymentRateAnnual.csv')
print('natl_unemploy_rate_df'); print(natl_unemploy_rate_df);print

'''
US Household Disposable Income
'''
us_household_disp_income_df = pd.read_csv('./covariates_raw/US_Household_Disposable_Income.csv')
print('us_household_disp_income_df'); print(us_household_disp_income_df);print

'''
US Household Savings
'''
us_household_savings_dr = pd.read_csv('./covariates_raw/US_Household_Savings.csv')
print('us_household_savings_dr'); print(us_household_savings_dr);print