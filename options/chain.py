# options/chain.py
import yfinance as yf
from rich.table import Table
from rich.console import Console

class OptionsAnalyzer:
    def __init__(self):
        self.console = Console()
        
    def get_chain(self, ticker, expiration=None):
        stock = yf.Ticker(ticker)
        exp_dates = stock.options
        
        if not expiration:
            expiration = exp_dates[0]
            
        opt = stock.option_chain(expiration)
        return self._create_table(opt.calls, opt.puts)

    def _create_table(self, calls, puts):
        table = Table(title="Options Chain", show_header=True)
        table.add_column("Strike", style="cyan")
        table.add_column("Call IV", style="green")
        table.add_column("Call Price", style="green")
        table.add_column("Put IV", style="red")
        table.add_column("Put Price", style="red")
        
        for _, (call, put) in enumerate(zip(calls.itertuples(), puts.itertuples())):
            table.add_row(
                f"{call.strike:.2f}",
                f"{call.impliedVolatility:.2%}",
                f"{call.lastPrice:.2f}",
                f"{put.impliedVolatility:.2%}",
                f"{put.lastPrice:.2f}"
            )
        return table