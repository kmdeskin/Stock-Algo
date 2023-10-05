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
In the main script or module where you need to use the API token (like algo.py), import it using the line:
  
  from secrets import API_TOKEN

### Running the algorithm 

To run the algorithm, execute algo.py in your terminal or IDE:
   
   python algo.py

### View the results 

After the algorithm completes, it will display the calculated number of shares to buy for each stock. You can use this information to make investment decisions.

## What is IEX cloud?!

[IEX Cloud](https://iexcloud.io/) is a financial data platform that provides access to a wide range of financial market data, including stock prices, market statistics, and more. This project utilizes IEX Cloud's API to fetch real-time and historical stock market data.

## How does the algorithm work?

I implemented multiple functions in this algorithm these include:

### fetch_stock_data 

The `fetch_stock_data` function is a utility within this project that allows you to retrieve stock information for a specified stock symbol using the IEX Cloud API. Here's how it works:

This function serves the purpose of fetching real-time stock data for analysis, reporting, or any other use. It takes a single argument, `symbol`, which should be a valid stock symbol, and it returns the stock information as a JSON object.

### calculate_rsi 

The `calculate_rsi` function is a Python function designed to calculate the Relative Strength Index (RSI) for a given set of historical price data. It uses the Technical Analysis Library (TA-Lib) to perform this calculation. Here's how it works:

### Purpose
The primary purpose of this function is to compute the RSI, a commonly used technical indicator in financial analysis. RSI measures the speed and change of price movements and is often used to identify overbought or oversold conditions in financial markets.

### Input
The function expects a single argument, `historical_data`, which should be a list of dictionaries. Each dictionary in the list represents historical price data, and it should contain at least a 'close' key-value pair representing the closing price for a specific time period.

### Output
The function returns the last calculated RSI value as a floating-point number.

### main 

The `main` function is a central component of this project, responsible for performing the following tasks:

### Purpose
The primary purpose of the `main` function is to create a portfolio of S&P 500 stocks based on a specified investment strategy. It reads stock data from a CSV file, calculates various metrics, and determines the number of shares to buy for each stock.

### Inputs
The function relies on the following inputs and dependencies:

1. **CSV Data**: It reads a CSV file named 'sp_500_stocks.csv' containing information about S&P 500 stocks using the Pandas library. This file likely includes stock symbols and other relevant data.

2. **Custom Columns**: It initializes a Pandas DataFrame with specific column names, including 'ticker', 'price', 'market capitalization', and 'number of shares to buy'.

3. **External Functions**: The `main` function calls two external functions:
   - `fetch_stock_data(symbol)`: This function fetches the latest stock data (including the latest price) for a given stock symbol.
   - `calculate_rsi(historical_data)`: This function calculates the Relative Strength Index (RSI) for a stock based on historical price data.

### Workflow
Here's a step-by-step breakdown of what the `main` function does:

1. **Reading CSV Data**: It reads the CSV file to obtain information about S&P 500 stocks and stores it in the 'stocks' variable.

2. **Iterating Over Stocks**: It iterates over each stock symbol in the CSV file.

3. **Fetching Stock Data**: For each stock, it fetches the latest stock data (including the latest price) using the `fetch_stock_data` function.

4. **Fetching Historical Data**: It fetches historical price data for the past year for that stock from the IEX Cloud API.

5. **Calculating RSI**: It calculates the Relative Strength Index (RSI) for the stock using the `calculate_rsi` function.

6. **Portfolio Weighting**: It calculates a combined weight for each stock based on RSI and equal weight. This determines how much of the portfolio should be allocated to each stock.

7. **Calculating Shares to Buy**: It calculates the number of shares to buy for each stock based on the user's portfolio value and the calculated weight.

8. **Building the DataFrame**: The results, including the stock symbol, latest price, market capitalization, and shares to buy, are appended to the Pandas DataFrame.

9. **Printing the Portfolio**: Finally, the resulting DataFrame is printed, displaying the calculated number of shares to buy for each stock.

### User Interaction
The `main` function interacts with the user to obtain portfolio value for each stock symbol. It validates user inputs and calculates positions accordingly.

### Note
- Ensure that you have the necessary dependencies, including Pandas, NumPy, and any custom functions (`fetch_stock_data` and `calculate_rsi`), set up correctly before running this function.

- Make sure you have API_TOKEN defined in your code to access external APIs.










