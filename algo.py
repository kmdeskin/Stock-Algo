#important necessary libraries 
import xlsxwriter #for creating excel files 
import pandas as pd #pandas data science library
import requests #for http requests
import math #math module
import talib #used to calculate RSI 
import numpy as np #numerical computing library

from secrets import API_TOKEN #import the api 
stocks = pd.read_csv('sp_500_stocks.csv') #read the stocks from CSV file and store data in a panda library 
symbol = 'GOOGL' #google symbol 
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={API_TOKEN}' #this constructs the URL for the API address
data = requests.get(api_url).json() #sends an HTTP GET request to to api url 
#the data variable contains important information about the stock like last traded price, market cap, etc. 
data #outputs the data dictionary

#data needs to be in a proper format 
data['latestprice']
data['marketcap']

#store this information in a table with certain characteristics 
mycolumns = ['Ticker', 'Price', 'Market Capitalization', 'Number Of Shares to Buy']
dataframe = pd.DataFrame(columns = mycolumns)

#create a series with the pandas array that accesses the lastest price and market cap and add new row to DataFrame 
dataframe = dataframe.append(pd.Series(['GOOGL', data['latestprice'], data['marketcap'], 'N/A'], index = mycolumns), ignore_index = True)
dataframe


