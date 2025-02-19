# financials/fundamental/earnings_quality.py
from data_sources.source_router import get_fundamentals
from rich.table import Table

class EarningsQuality:
    @staticmethod
    def score(ticker):
        accruals = (net_income - cash_flow) / total_assets
        return 1 - (accruals / abs(net_income))