# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:43:10 2023

@author: Michael
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

def extractGDPdf(file_path):
    # Read the Excel file into a DataFrame
    sdg = pd.read_csv(file_path)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name', 'Series Code'] + [str(year) for year in range(2000, 2020)]

    # Extract relevant columns
    sdg_df = sdg[sdg['Series Code'] == 'NY.GDP.MKTP.KD.ZG'][columns_extract]

    # Define countries to filter
    countries = ['CEB', 'EAS', 'ECS', 'LCN', 'MEA', 'NAC', 'SAS', 'SSF']

    # Filter rows based on countries
    sdg_df = sdg_df[sdg_df['Country Code'].isin(countries)]

    # Select specific columns
    sdg_df = sdg_df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Set 'Country Name' as the index
    sdg_df.set_index('Country Name', inplace=True)

    # Transpose the DataFrame
    sdg_df_T = sdg_df.transpose()

    return sdg_df, sdg_df_T

# Provide the correct file path to your Excel file
file_path = 'sdg df.csv'

# Call the function with the file path
sdg_df, sdg_df_T = extractGDPdf(file_path)

# Display the DataFrames
print("Original GDP Growth DataFrame:")
print(sdg_df)
print("\nTransposed GDP Growth DataFrame:")
print(sdg_df_T)

def extractUrbanPop_df(file_path2):
    # Read the Excel file into a DataFrame
    urban_pop = pd.read_csv(file_path2)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name', 'Series Code'] + [str(year) for year in range(2000, 2020)]

    # Extract relevant columns
    urban_pop = urban_pop[urban_pop['Series Code'] == 'SP.URB.TOTL.IN.ZS'][columns_extract]

    # Define countries to filter
    countries = ['CEB', 'EAS', 'ECS', 'LCN', 'MEA', 'NAC', 'SAS', 'SSF']

    # Filter rows based on countries
    urban_pop = urban_pop[urban_pop['Country Code'].isin(countries)]

    # Select specific columns
    urban_pop = urban_pop.drop(['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Set 'Country Name' as the index
    urban_pop.set_index('Country Name', inplace=True)
    urban_pop = urban_pop.astype('float64')

    # Transpose the DataFrame
    urban_pop_T = urban_pop.transpose()

    return urban_pop, urban_pop_T

file_path2 = 'sdg df.csv'

# Call the function with the file path
urban_pop, urban_pop_T = extractUrbanPop_df(file_path)

# Display the DataFrames
print("Original Urban Population Percentage DataFrame:")
print(urban_pop)
print("\nTransposed Urban Population Percentage DataFrame:")
print(urban_pop_T)



def extractFemaleInIndustrydf(file_path3):
    # Read the Excel file into a DataFrame
    fem_industry = pd.read_csv(file_path3)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name', 'Series Code'] + [str(year) for year in range(2000, 2020)]

    # Extract relevant columns
    fem_industry = fem_industry[fem_industry['Series Code'] == 'SL.IND.EMPL.FE.ZS'][columns_extract]

    # Define countries to filter
    countries = ['CEB', 'EAS', 'ECS', 'LCN', 'MEA', 'NAC', 'SAS', 'SSF']

    # Filter rows based on countries
    fem_industry = fem_industry[fem_industry['Country Code'].isin(countries)]

    # Select specific columns
    fem_industry = fem_industry.drop(['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Set 'Country Name' as the index
    fem_industry.set_index('Country Name', inplace=True)
    fem_industry = fem_industry.astype('float64')

    # Transpose the DataFrame
    fem_industry_T = fem_industry.transpose()

    return fem_industry, fem_industry_T

# Provide the correct file path to your Excel file
file_path3 = 'sdg df.csv'

# Call the function with the file path
fem_industry, fem_industry_T = extractFemaleInIndustrydf(file_path3)

# Display the DataFrames
print("Original Percentage Female in Industry DataFrame:")
print(fem_industry)
print("\nTransposed Percentage Female in Industry DataFrame:")
print(fem_industry_T)


def extractMaleInIndustrydf(file_path4):
    # Read the Excel file into a DataFrame
    male_industry = pd.read_csv(file_path3)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name', 'Series Code'] + [str(year) for year in range(2000, 2020)]

    # Extract relevant columns
    male_industry = male_industry[male_industry['Series Code'] == 'SL.IND.EMPL.MA.ZS'][columns_extract]

    # Define countries to filter
    countries = ['CEB', 'EAS', 'ECS', 'LCN', 'MEA', 'NAC', 'SAS', 'SSF']

    # Filter rows based on countries
    male_industry = male_industry[male_industry['Country Code'].isin(countries)]

    # Select specific columns
    male_industry = male_industry.drop(['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Set 'Country Name' as the index
    male_industry.set_index('Country Name', inplace=True)
    male_industry = male_industry.astype('float64')

    # Transpose the DataFrame
    male_industry_T = male_industry.transpose()

    return male_industry, male_industry_T

# Provide the correct file path to your Excel file
file_path4 = 'sdg df.csv'

# Call the function with the file path
male_industry, male_industry_T = extractMaleInIndustrydf(file_path3)

# Display the DataFrames
print("Original Percentage Male in Industry DataFrame:")
print(male_industry)
print("\nTransposed Percentage Male in Industry DataFrame:")
print(male_industry_T)




print(urban_pop.describe())

print(urban_pop_T.columns)

plt.figure()

plt.plot(fem_industry_T.index, fem_industry_T[fem_industry_T.columns], label=fem_industry_T.columns)
plt.xticks(rotation=90)
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(male_industry_T.index, male_industry_T[male_industry_T.columns])
plt.xticks(rotation=90)
plt.grid()
plt.show()

print(urban_pop_T.mean())
