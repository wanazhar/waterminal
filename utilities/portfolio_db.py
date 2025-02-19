# utilities/portfolio_db.py
import sqlite3
import pandas as pd
from pathlib import Path
from contextlib import contextmanager
from typing import Generator

class PortfolioDB:
    def __init__(self):
        self.db_path = Path.home() / ".waterminal" / "portfolio.db"
        self._init_db()

    @contextmanager
    def connection(self) -> Generator[sqlite3.Connection, None, None]:
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def _init_db(self):
        with self.connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS positions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    shares REAL NOT NULL,
                    entry_price REAL NOT NULL,
                    entry_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    source TEXT DEFAULT 'manual'
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    shares REAL NOT NULL,
                    price REAL NOT NULL,
                    trans_type TEXT CHECK(trans_type IN ('BUY', 'SELL')),
                    trans_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def get_portfolio(self) -> pd.DataFrame:
        with self.connection() as conn:
            return pd.read_sql("""
                SELECT symbol, SUM(shares) as total_shares, 
                AVG(entry_price) as avg_cost
                FROM positions
                GROUP BY symbol
                HAVING total_shares > 0
            """, conn)