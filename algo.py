#import necessary libraries 
import pandas as pd 
import requests 
import talib
import numpy as np
import math
from secrets import API_TOKEN

def fetch_stock_data(symbol):
    #this function takes a stock symbol as input and makes an HTTP GET request to the IEX Cloud API to fetch information about the stock
    #it returns the data as a JSON object
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={API_TOKEN}'
    data = requests.get(api_url).json()
    return data

def calculate_rsi(historical_data):
    #this function calculates the Relative Strength Index (RSI) for a given historical price data
    #it extracts closing prices from the historical data, calculates the RSI using talib with a time period of 14, and returns the last RSI value
    closing_prices = [item['close'] for item in historical_data]
    return talib.RSI(np.array(closing_prices), timeperiod=14)[-1]

def main():
    #read a CSV file ('sp_500_stocks.csv') containing information about S&P 500 stocks using pandas
    stocks = pd.read_csv('sp_500_stocks.csv')
    #initializes a pandas DataFrame with specific column names
    mycolumns = ['ticker', 'price', 'market capitalization', 'number of shares to buy']
    dataframe = pd.DataFrame(columns=mycolumns)

    #iterate over each stock symbol in the CSV file
    for symbol in stocks['ticker']:
        #fetch the latest stock data (including the latest price) using the fetch_stock_data function
        data = fetch_stock_data(symbol)
        #fetch historical price data for the past year for that stock
        historical_data = requests.get(f'https://sandbox.iexapis.com/stable/stock/{symbol}/chart/1y?token={API_TOKEN}').json()
        #calculate the RSI for the stock using the calculate_rsi function
        rsi = calculate_rsi(historical_data)

        #calculate the combined weight (e.g., 70% based on RSI, 30% equal weight)
        rsi_weight = 0.7 if rsi < 30 else (0.3 if rsi > 70 else 0.5)
        equal_weight = 1 / len(stocks)
        combined_weight = 0.7 * rsi_weight + 0.3 * equal_weight

        #calculate the position in each stock based on the user's portfolio value and the weight
        portfolio = input(f"enter the value of your portfolio for {symbol}: ")
        try:
            val = float(portfolio)
        except ValueError:
            print(f"that's not a number! please try again for {symbol}.")
            continue

        position = val * combined_weight
        shares_to_buy = math.floor(position / data['latestprice'])

        #append the results to the DataFrame
        dataframe = dataframe.append(pd.Series([symbol, data['latestprice'], data['marketcap'], shares_to_buy], index=mycolumns), ignore_index=True)

    #print the resulting DataFrame, which includes the calculated number of shares to buy for each stock
    print(dataframe)

if __name__ == "__main__":
    main()
