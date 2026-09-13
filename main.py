### Goal of this project is to collect and analyze data about the performance of different publicly traded companies. The data will be collected from various financial APIs and will include metrics such as stock prices, revenue, profit margins, and other key performance indicators. The analysis will help identify trends, compare companies within the same industry, and provide insights for investors and stakeholders.

import yfinance as yf #getting data from yahoo finance
import pandas as pd #data manipulation and analysis
import matplotlib.pyplot as plt #data visualization


def get_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for a given ticker symbol from Yahoo Finance.

    Parameters:
    ticker (str): The stock ticker symbol (e.g., 'RY.TO' for Royal Bank of Canada).
    start_date (str): The start date for the data in 'YYYY-MM-DD' format.
    end_date (str): The end date for the data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the historical stock data.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def stock_variance(stock_data):
    """
    Calculate the variance of the stock's closing prices.

    Parameters:
    stock_data (pd.DataFrame): A DataFrame containing the historical stock data.

    Returns:
    float: The variance of the stock's closing prices.
    """
    return stock_data['Close'].var()

def stock_volatility(stock_data):
    """
    Calculate the volatility of the stock's closing prices.

    Parameters:
    stock_data (pd.DataFrame): A DataFrame containing the historical stock data.

    Returns:
    float: The volatility of the stock's closing prices.
    """
    return stock_data['Close'].std()

def stock_return(stock_data):
    """
    Calculate the return of the stock's closing prices.

    Parameters:
    stock_data (pd.DataFrame): A DataFrame containing the historical stock data.

    Returns:
    float: The return of the stock's closing prices.
    """
    return (stock_data['Close'][-1] - stock_data['Close'][0]) / stock_data['Close'][0]


def open_earliest_to_close_latest_difference(stock_data):
    """
    Calculate the difference between the opening price on the earliest date
    and the closing price on the latest date.

    Parameters:
    stock_data (pd.DataFrame): A DataFrame containing the historical stock data.

    Returns:
    float: The difference between the earliest Open and latest Close.
    """
    earliest_open = stock_data['Open'].iloc[0]
    latest_close = stock_data['Close'].iloc[-1]
    return latest_close - earliest_open


def __main__():
    rbc_data = get_stock_data('RY.TO', '2020-01-01', '2023-01-01')
    td_data = get_stock_data('TD.TO', '2020-01-01', '2023-01-01')
    cibc_data = get_stock_data('CM.TO', '2020-01-01', '2023-01-01') 
    sb_data = get_stock_data('BNS.TO', '2020-01-01', '2023-01-01')
    nb_data = get_stock_data('NA.TO', '2020-01-01', '2023-01-01')
    bmo_data = get_stock_data('BMO.TO', '2020-01-01', '2023-01-01')
    data_list = [rbc_data, td_data, cibc_data, sb_data, nb_data, bmo_data]

    for x in data_list:
        print(f"Variance: {stock_variance(x)}")
        print(f"Volatility: {stock_volatility(x)}")
        print(f"Open at earliest date vs Close at latest date difference: {open_earliest_to_close_latest_difference(x)}")
        #print(f"Return: {stock_return(x)}")


if __name__ == "__main__":
    __main__()