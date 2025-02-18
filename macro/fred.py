# macro/fred.py
from fredapi import Fred
from config.core import Config
from rich.table import Table

fred = Fred(api_key=Config.API_KEYS['fred'])

class MacroData:
    SERIES_MAP = {
        'GDP': 'GDPC1',
        'UNRATE': 'UNRATE',
        'CPI': 'CPIAUCSL',
        'FEDFUNDS': 'FEDFUNDS'
    }
    
    @classmethod
    def get_series(cls, series_id, **kwargs):
        return fred.get_series(series_id, **kwargs)
        
    @classmethod
    def economic_dashboard(cls):
        table = Table(title="Macroeconomic Dashboard")
        table.add_column("Indicator", style="cyan")
        table.add_column("Current", style="magenta")
        table.add_column("1Y Change", style="green")
        
        for name, code in cls.SERIES_MAP.items():
            data = cls.get_series(code)
            current = data[-1]
            yoy = (current/data[-252]-1)*100  # 252 trading days
            
            table.add_row(
                name,
                f"{current:.2f}",
                f"{yoy:.2f}%"
            )
        return table