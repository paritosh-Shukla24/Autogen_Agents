# filename: ytd_stock_plot.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    """ Fetch stock data from Yahoo Finance """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Adj Close']

def calculate_ytd_gain(data):
    """ Calculate the YTD gain as a percentage """
    ytd_start = data.iloc[0]  # Price at the start of the year
    return (data / ytd_start - 1) * 100

def plot_data(nvda_gains, tsla_gains):
    """ Plot the YTD stock gains for NVDA and TSLA """
    plt.figure(figsize=(10, 5))
    plt.plot(nvda_gains.index, nvda_gains, label="NVDA YTD Gain %")
    plt.plot(tsla_gains.index, tsla_gains, label="TSLA YTD Gain %")
    plt.title("YTD Stock Gains for NVDA and TSLA")
    plt.xlabel("Date")
    plt.ylabel("Gain %")
    plt.legend()
    plt.grid(True)
    plt.savefig('ytd_stock_gains.png')
    plt.show()

# Set the date range for YTD 2024
start_date = '2024-01-01'
end_date = '2024-11-02'

# Fetch stock data
nvda_data = fetch_stock_data('NVDA', start_date, end_date)
tsla_data = fetch_stock_data('TSLA', start_date, end_date)

# Calculate the YTD gains
nvda_gains = calculate_ytd_gain(nvda_data)
tsla_gains = calculate_ytd_gain(tsla_data)

# Plot the data
plot_data(nvda_gains, tsla_gains)