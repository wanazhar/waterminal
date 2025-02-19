# portfolio/manager.py
import pandas as pd
from rich.console import Console
from rich.table import Table
from utilities.portfolio_db import PortfolioDB
from data_sources.source_router import get_live_price
from typing import Dict

class PortfolioManager:
    def __init__(self):
        self.db = PortfolioDB()
        self.console = Console()
        self.historical = pd.DataFrame()

    def add_position(self, symbol: str, shares: float, entry_price: float):
        """Add or update a position in the portfolio"""
        with self.db.connection() as conn:
            conn.execute("""
                INSERT INTO positions (symbol, shares, entry_price)
                VALUES (?, ?, ?)
            """, (symbol, shares, entry_price))
            conn.commit()

    async def update_prices(self):
        """Update market prices for all positions"""
        positions = self.db.get_portfolio()
        symbols = positions['symbol'].tolist()
        live_data = await DataPipeline.get_live_prices(symbols)
        
        # Store updated prices in historical data
        self.historical = pd.concat([
            self.historical,
            pd.DataFrame(live_data, columns=['symbol', 'price', 'timestamp'])
        ])

    def performance_report(self) -> Table:
        """Generate comprehensive performance analysis"""
        positions = self.db.get_portfolio()
        positions['current_price'] = positions['symbol'].apply(get_live_price)
        
        metrics = {
            'Total Value': self._calculate_total_value(positions),
            'Daily Return': self._calculate_daily_return(),
            'YTD Return': self._calculate_ytd_return(),
            'Volatility (30d)': self._calculate_volatility(),
            'Sharpe Ratio': self._calculate_sharpe_ratio()
        }
        
        return self._create_performance_table(metrics)

    def _calculate_total_value(self, positions: pd.DataFrame) -> float:
        return (positions['total_shares'] * positions['current_price']).sum()

    def _calculate_daily_return(self) -> float:
        if not self.historical.empty:
            latest = self.historical.groupby('symbol').last()
            prev_close = latest.groupby('symbol')['price'].shift(1)
            return (latest['price'] - prev_close).mean()
        return 0.0

    def _calculate_ytd_return(self) -> float:
        # Implementation requires historical data
        return 0.0  # Placeholder

    def _calculate_volatility(self) -> float:
        if not self.historical.empty:
            returns = self.historical.pivot(
                index='timestamp', 
                columns='symbol', 
                values='price'
            ).pct_change().std()
            return returns.mean()
        return 0.0

    def _calculate_sharpe_ratio(self) -> float:
        if not self.historical.empty:
            avg_return = self.historical['price'].pct_change().mean()
            std_dev = self.historical['price'].pct_change().std()
            return avg_return / std_dev
        return 0.0

    def _create_performance_table(self, metrics: Dict) -> Table:
        table = Table(title="Portfolio Performance", show_header=True)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        
        for name, value in metrics.items():
            if isinstance(value, float):
                table.add_row(name, f"{value:.2%}" if name.endswith('Return') else f"${value:,.2f}")
            else:
                table.add_row(name, str(value))
                
        return table

    def get_portfolio_view(self) -> Table:
        """Get current portfolio summary table"""
        df = self.db.get_portfolio()
        df['current_price'] = df['symbol'].apply(get_live_price)
        df['value'] = df['total_shares'] * df['current_price']
        df['pnl'] = (df['current_price'] - df['avg_cost']) / df['avg_cost']
        
        return self._create_portfolio_table(df)

    def _create_portfolio_table(self, df: pd.DataFrame) -> Table:
        table = Table(title="Portfolio Summary", show_lines=True)
        table.add_column("Symbol", style="cyan")
        table.add_column("Shares", style="magenta")
        table.add_column("Avg Cost", style="green")
        table.add_column("Price", style="yellow")
        table.add_column("Value", style="blue")
        table.add_column("PnL %", style="red")
        
        for _, row in df.iterrows():
            table.add_row(
                row['symbol'],
                f"{row['total_shares']:.2f}",
                f"${row['avg_cost']:.2f}",
                f"${row['current_price']:.2f}",
                f"${row['value']:,.2f}",
                f"{row['pnl']:.2%}"
            )
        return table