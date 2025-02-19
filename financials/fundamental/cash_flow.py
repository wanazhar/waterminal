# financials/fundamental/cash_flow.py
from data_sources.source_router import get_fundamentals
from rich.table import Table

class CashFlowAnalyzer:
    @staticmethod
    def analyze(ticker: str) -> Table:
        """Analyze cash flow statement"""
        cf = get_fundamentals(ticker, 'cash_flow')
        income = get_fundamentals(ticker, 'income')
        
        metrics = {
            'OCF/Net Income': cf['OperatingCashFlow'] / income['NetIncome'],
            'FCF Yield': cf['FreeCashFlow'] / get_market_cap(ticker),
            'Capex/Sales': abs(cf['CapitalExpenditure']) / income['Revenue']
        }
        
        return CashFlowAnalyzer._create_table(ticker, metrics)

    @staticmethod
    def _create_table(ticker: str, metrics: Dict) -> Table:
        table = Table(title=f"Cash Flow Analysis - {ticker}")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        
        for name, value in metrics.items():
            table.add_row(name, f"{value:.2f}")
        return table