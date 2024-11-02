# filename: fetch_and_plot_stocks.py
from functions import get_stock_prices, plot_stock_prices
import pandas as pd

# Define the start and end dates for YTD
start_date = '2024-01-01'
end_date = '2024-11-02'  # Today's date

# Stock symbols of interest
stock_symbols = ['NVDA', 'TSLA']

# Fetching stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plotting the stock prices and saving to a file
plot_stock_prices(stock_prices, filename='stock_prices_YTD_plot.png')