# portfolio/manager.py
import numpy as np
import pandas as pd
from rich.console import Console
from rich.table import Table

class PortfolioManager:
    def __init__(self):
        self.positions = {}
        self.historical = pd.DataFrame()
        self.console = Console()
        
    def add_position(self, symbol, shares, entry_price):
        self.positions[symbol] = {
            'shares': shares,
            'entry': entry_price,
            'current': entry_price
        }
        
    async def update_prices(self):
        symbols = list(self.positions.keys())
        live_data = await DataPipeline.get_live_prices(symbols)
        for symbol, price in live_data.items():
            self.positions[symbol]['current'] = price
            
    def performance_report(self):
        table = Table(title="Portfolio Performance", show_header=True)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        
        returns = self._calculate_returns()
        volatility = self._calculate_volatility()
        
        table.add_row("Total Value", f"${self.total_value:,.2f}")
        table.add_row("Daily Return", f"{returns['daily']:.2%}")
        table.add_row("YTD Return", f"{returns['ytd']:.2%}")
        table.add_row("Volatility (30d)", f"{volatility:.2%}")
        table.add_row("Sharpe Ratio", f"{self.sharpe_ratio:.2f}")
        
        self.console.print(table)
        
    def _calculate_returns(self):
        # Implement portfolio return calculations
        pass