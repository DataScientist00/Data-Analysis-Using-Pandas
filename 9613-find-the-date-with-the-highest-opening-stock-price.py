#problem link--->> https://platform.stratascratch.com/coding/9613-find-the-date-with-the-highest-opening-stock-price?code_type=2


# Import your libraries
import pandas as pd
import datetime as dt

# Start writing code
aapl_historical_stock_price['date'] = aapl_historical_stock_price['date'].dt.strftime('%Y-%m-%d')
aapl_historical_stock_price[aapl_historical_stock_price['open'] == aapl_historical_stock_price['open'].max()][['date']]
