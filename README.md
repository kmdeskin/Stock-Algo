# Stock-Algo

In this project, I've developed a trading algorithm that combines an equal-weight strategy with the Relative Strength Index (RSI) for the S&P 500.

## Introduction

Trading algorithms are a popular tool for automating the investment process, and this project focuses on creating a versatile algorithm for trading the S&P 500. The algorithm incorporates two main components: equal weight allocation and the Relative Strength Index (RSI).

### Equal Weight Algorithm

The equal weight algorithm assigns an equal portion of the investment to each stock in the S&P 500 index. This strategy aims to provide a balanced and diversified investment approach.

### Relative Strength Index (RSI)

The RSI is a momentum indicator that helps assess whether a stock or market is overbought or oversold. By incorporating RSI, our algorithm aims to make informed decisions based on market momentum.

## Features

- Equal weight allocation strategy for S&P 500 stocks.
- Integration of the Relative Strength Index (RSI) for market momentum analysis.

## Usage Instructions 

Follow the steps below to use the algorithm:

### Prerequisites

Before you begin, ensure you have Python and the required libraries installed. 
Required libraries:

- pandas: used for handling stock data and creating DataFrames to organize and process data.
- requests: used to send requests to the IEX Cloud API to fetch stock information, including the latest prices and historical data.
- talib: use talib to calculate technical indicators like the Relative Strength Index (RSI) for stocks based on historical price data. 
- numpy: used for various numerical operations, especially when working with historical stock price data.
- math: used for rounding down the number of shares to buy based on portfolio value and stock price.

### API Token Storage

To keep sensitive information like your API token secure, use a `secrets.py` file to store it. Follow these steps to set up your own `secrets.py` file:

1. Create a file named `secrets.py` in the project's root directory if it doesn't already exist.

2. Inside `secrets.py`, define your API token like this:

   API_TOKEN = 'your-api-token-here'

Make sure to replace 'your-api-token-here' with your actual API token.
In the main script or module where you need to use the API token (like main.py), import it using the line:
  
  from secrets import API_TOKEN

### Running the algorithm 

To run the algorithm, execute algo.py in your terminal or IDE:
   
   python algo.py

### View the results 

After the algorithm completes, it will display the calculated number of shares to buy for each stock. You can use this information to make investment decisions.

## What is IEX cloud?!

[IEX Cloud](https://iexcloud.io/) is a financial data platform that provides access to a wide range of financial market data, including stock prices, market statistics, and more. This project utilizes IEX Cloud's API to fetch real-time and historical stock market data.





