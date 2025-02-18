# profile_viewer.py
import yfinance as yf
from tabulate import tabulate

def view_company_profile(ticker):
    company = yf.Ticker(ticker)
    info = company.info
    
    profile_data = {
        'Name': info.get('longName', 'N/A'),
        'Sector': info.get('sector', 'N/A'),
        'Industry': info.get('industry', 'N/A'),
        'Employees': info.get('fullTimeEmployees', 'N/A'),
        'Market Cap': f"{info.get('marketCap', 'N/A'):,}",
        'CEO': info.get('ceo', 'N/A'),
        'Website': info.get('website', 'N/A'),
        'Summary': info.get('longBusinessSummary', 'N/A')[:200] + '...'
    }
    
    table = [[k, v] for k, v in profile_data.items()]
    print(f"\n{ticker} Company Profile:")
    print(tabulate(table, headers=['Field', 'Value'], tablefmt='grid'))