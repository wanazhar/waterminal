# historical.py
import yfinance as yf
from tabulate import tabulate

def fetch_historical_prices(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')
    
    for ticker in tickers:
        print(f"\n{ticker} Historical Prices:")
        df = data[ticker][['Open', 'High', 'Low', 'Close', 'Volume']]
        print(tabulate(df, headers='keys', tablefmt='psql'))