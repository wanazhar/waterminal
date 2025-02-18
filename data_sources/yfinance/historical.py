# data_sources/yfinance/historical.py
import yfinance as yf
from rich.table import Table

def get_historical(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    table = Table(title=f"Historical Data - {ticker}")
    # Add table columns and rows
    return table