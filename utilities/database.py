# utilities/database.py
import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path.home() / ".waterminal" / "portfolio.db"

class PortfolioDB:
    @contextmanager
    def _connection(self):
        conn = sqlite3.connect(DB_PATH)
        try:
            yield conn
        finally:
            conn.close()
            
    def _migrate(self):
        with self._connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS positions (
                    id INTEGER PRIMARY KEY,
                    symbol TEXT,
                    shares REAL,
                    entry_price REAL,
                    entry_date DATE,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
    def __init__(self):
        DB_PATH.parent.mkdir(exist_ok=True)
        self._migrate()