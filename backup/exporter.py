# exporter.py
import yfinance as yf
import pandas as pd
from datetime import datetime

def export_to_excel(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')
    
    today = datetime.now().strftime("%d%m%Y")
    filename = f"export_{today}.xlsx"
    
    with pd.ExcelWriter(filename) as writer:
        for ticker in tickers:
            df = data[ticker][['Open', 'High', 'Low', 'Close', 'Volume']]
            df.to_excel(writer, sheet_name=ticker[:31])
    
    print(f"\nData exported to {filename} successfully!")