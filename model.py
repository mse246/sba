import csv
import numpy as np
import pandas as pd
import datetime

###################
# Reading in data #
###################
df = pd.read_csv('SBA_Loan_data_.csv',)
# approval_dates = df.iloc[:]['ApprovalDate']
# print(approval_dates)

print(df)
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
fed_funds_series = pd.read_csv('./covariates_raw/FEDFUNDS.csv')

for index, row in fed_funds_series.iterrows():
    if index <= 288:
        col_name = "FedFundRate_month_%s" % (index)
        df[col_name] = row['FEDFUNDS']

'''
Savings Rates
'''
savings_rates_series = pd.read_csv('./covariates_raw/SavingsRate.csv')
for index, row in savings_rates_series.iterrows():
    if index <= 288:
        col_name = "SavingsRate_month_%s" % (index)
        df[col_name] = row['PSAVERT']

'''
US Dollar Index
'''
us_dollar_index_series = pd.read_csv('./covariates_raw/us-dollar-index-historical-chart.csv')
for index, row in us_dollar_index_series.iterrows():
    if index <= 288:
        col_name = "USDIndex_month_%s" % (index)
        df[col_name] = row[' value']

# '''
# Housing Prices
# '''
# # housing_prices_series = pd.read_csv('./covariates_raw/Zip_MedianValuePerSqft_AllHomes.csv')
# # for index, row in housing_prices_series.iterrows():
# #     if index <= 288:
# #         col_name = "USDIndex_month_%s" % (index)
# #         df[col_name] = row[' value']
# # print df

'''
US Import Price Index
'''
us_import_price_index_series = pd.read_csv('./covariates_raw/US_Import_Price_Index.csv')
for index, row in us_import_price_index_series.iterrows():
    if index <= 288:
        col_name = "USImportPriceIndex_month_%s" % (index)
        df[col_name] = row['US Import Price Indexes for Selected Categories of Goods (Monthly)']

'''
US Uncertainty Index
'''
us_uncertainty_index_series = pd.read_csv('./covariates_raw/US_Uncertainty_Index.csv')
for index, row in us_uncertainty_index_series.iterrows():
    if index <= 288:
        col_name = "USUncertaintyIndexBaseline_month_%s" % (index)
        df[col_name] = row['US Economic Policy Uncertainty Index (Monthly - Baseline)']

for index, row in us_uncertainty_index_series.iterrows():
    if index <= 288:
        col_name = "USUncertaintyIndexNews_month_%s" % (index)
        df[col_name] = row['US Economic Policy Uncertainty Index (Monthly - News Based)']

'''
Small Business Confidence
'''
sm_business_conf_series = pd.read_csv('./covariates_raw/Small_business_confidence.csv')
for index, row in sm_business_conf_series.iterrows():
    if index <= 288:
        col_name = "SmallBusinessConfidence_month_%s" % (index)
        df[col_name] = row['Small Business Optimism']

'''
Crisis Indicator
'''
crisis_indicator_series = pd.read_csv('./covariates_raw/crisisindicator.csv')
for index, row in crisis_indicator_series.iterrows():
    if index <= 288:
        col_name = "CrisisIndicator_month_%s" % (index)
        df[col_name] = row[' value']

'''
National Unemployement Rate
'''
natl_unemploy_rate_series = pd.read_csv('./covariates_raw/NationalUnemploymentRateAnnual.csv')
for index, row in natl_unemploy_rate_series.iterrows():
    for i in range(0, 12):
        if (index*12)+i <= 288:
            col_name = "UnemploymentRate_month_%s" % ((index*12)+i)
            df[col_name] = row['Unemployment rate']

'''
US Household Disposable Income
'''
us_household_disp_income_series = pd.read_csv('./covariates_raw/US_Household_Disposable_Income.csv')
for index, row in us_household_disp_income_series.iterrows():
    if index <= 288:
        col_name = "HouseholdDisposableIncome_month_%s" % (index)
        df[col_name] = row['Household Disposable Income (% Growth Rate)']

'''
US Household Savings
'''
us_household_savings_series = pd.read_csv('./covariates_raw/US_Household_Savings.csv')
for index, row in us_household_savings_series.iterrows():
    if index <= 288:
        col_name = "HouseholdSavings_month_%s" % (index)
        df[col_name] = row['Household Savings (% of Household Disposable Income)']

df.to_csv('SBA_Loan_data_with_covariates_.csv', encoding='utf-8', index=False)
