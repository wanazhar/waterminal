# technical/fibonacci.py
import pandas as pd
from rich.table import Table
from typing import Dict

class FibonacciRetracement:
    @staticmethod
    def calculate(data: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate Fibonacci retracement levels from historical data
        """
        max_price = data['High'].max()
        min_price = data['Low'].min()
        diff = max_price - min_price
        
        return {
            '0%': max_price,
            '23.6%': max_price - diff * 0.236,
            '38.2%': max_price - diff * 0.382,
            '50%': max_price - diff * 0.5,
            '61.8%': max_price - diff * 0.618,
            '100%': min_price
        }

    @staticmethod
    def display_levels(levels: Dict[str, float], ticker: str) -> Table:
        """Create Rich table for display"""
        table = Table(title=f"Fibonacci Levels - {ticker}", show_header=False)
        table.add_column("Level", style="cyan")
        table.add_column("Price", style="magenta")
        
        for level, price in levels.items():
            table.add_row(level, f"${price:.2f}")
            
        return table