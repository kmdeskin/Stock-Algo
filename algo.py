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

#store the data for all stocks in the dataframe using a for loop 
dataframe = pd.DataFrame(columns = mycolumns)
for symbol in stocks['Ticker']: #this is the for loop
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={API_TOKEN}'
    data = requests.get(api_url).json()
    dataframe = dataframe.append(pd.Series(['GOOGL', data['latestprice'], data['marketcap'], 'N/A'], index = mycolumns), ignore_index = True)

#now, in order to speed up the process, implement batch API calls instead of individually assessing each stock out of the 500 
#create a utility function that splits a list up into smaller chunks to create sublists 
#because IEX cloud lets you make batch calls in 100 tickers per request, there will be 500/100 = 5 groups to save time 
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

#after this function is created, the new sublists can be made
sublists = list(chunks(stocks['Ticker'], 100))
strings = []
for i in range(0, len(sublists)):
    strings.append(','.join(sublists[i]))
dataframe = pd.DataFrame(columns = mycolumns)
for string in strings: #implement the new sublists in the for loop to access the stock information 
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={API_TOKEN}'
    data = requests.get(api_url).json()
    for symbol in string.split(','):
        dataframe = dataframe.append(pd.Series(['GOOGL', data['latestprice'], data['marketcap'], 'N/A'], index = mycolumns), ignore_index = True)


#now the number of shares to buy can be calculated
#let the user determine how big the stock portfolio should be  
portfolio = input("enter the value of your portfolio: ")
try:
    val = float(portfolio)
except ValueError:
    print("that's not a number! \n try again:")
    portfolio = input("enter the value of your portfolio:")
#this is the algorithm 
position = float(portfolio) / len(dataframe.index)
for i in range(0, len(dataframe['Ticker'])-1):
    dataframe.loc[i, 'Number Of Shares to Buy'] = math.floor(position / dataframe['Price'][i])
dataframe








