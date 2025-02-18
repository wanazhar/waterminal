# financials/ratios/profitability.py
from data_sources.source_router import get_fundamentals
from rich.table import Table

class ProfitabilityRatios:
    @staticmethod
    def calculate(ticker):
        income = get_fundamentals(ticker, 'income')
        balance = get_fundamentals(ticker, 'balance')
        
        ratios = {
            'ROE': income['NetIncome'] / balance['Equity'],
            'ROA': income['NetIncome'] / balance['TotalAssets'],
            'Gross Margin': income['GrossProfit'] / income['Revenue'],
            'Operating Margin': income['OperatingIncome'] / income['Revenue']
        }
        
        return ProfitabilityRatios._create_table(ticker, ratios)
        
    @staticmethod
    def _create_table(ticker, ratios):
        table = Table(title=f"Profitability Ratios - {ticker}")
        table.add_column("Ratio", style="cyan")
        table.add_column("Value", style="magenta")
        
        for name, value in ratios.items():
            table.add_row(name, f"{value:.2%}")
            
        return table