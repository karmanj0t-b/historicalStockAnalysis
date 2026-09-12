### Goal of this project is to collect and analyze data about the performance of different publicly traded companies. The data will be collected from various financial APIs and will include metrics such as stock prices, revenue, profit margins, and other key performance indicators. The analysis will help identify trends, compare companies within the same industry, and provide insights for investors and stakeholders.

import yfinance as yf #getting data from yahoo finance
import pandas as pd #data manipulation and analysis
import matplotlib.pyplot as plt #data visualization


def get_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for a given ticker symbol from Yahoo Finance.

    Parameters:
    ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple).
    start_date (str): The start date for the data in 'YYYY-MM-DD' format.
    end_date (str): The end date for the data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the historical stock data.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

stock_data = get_stock_data('AAPL', '2020-01-01', '2023-01-01')

print(stock_data.head())  # Display the first few rows of the stock data