# financials/ratios/valuation.py
from data_sources.source_router import get_financials
from utilities.display import create_table

def show_valuation_ratios(ticker):
    income = get_financials(ticker, 'income')
    balance = get_financials(ticker, 'balance')
    
    ratios = {
        'P/E Ratio': calculate_pe(income, market_data),
        'EV/EBITDA': calculate_ev_ebitda(income, balance),
        'P/B Ratio': calculate_pb(balance, market_data)
    }
    
    create_table(
        title=f"Valuation Ratios - {ticker}",
        columns=["Ratio", "Value", "Industry Avg"],
        rows=[[k, v, get_industry_avg(k)] for k,v in ratios.items()]
    )