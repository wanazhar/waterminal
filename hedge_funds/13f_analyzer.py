# hedge_funds/13f_analyzer.py
from sec_edgar_downloader import Downloader
from rich.table import Table
import xmltodict
import os

class SEC13FAnalyzer:
    def __init__(self):
        self.dl = Downloader("waterminal", "user@waterminal.com")
        self.cache_dir = os.path.expanduser("~/.waterminal/13f")
        
    def get_top_holdings(self, cik: str, top_n: int = 10) -> Table:
        """Get top holdings from latest 13F filing"""
        self.dl.get("13F", cik, download_folder=self.cache_dir)
        filing = self._get_latest_filing(cik)
        positions = self._parse_filing(filing)
        
        return self._create_holdings_table(positions[:top_n])

    def _get_latest_filing(self, cik: str) -> str:
        # Implementation for finding latest XML filing
        pass

    def _parse_filing(self, filing_path: str) -> list:
        with open(filing_path) as f:
            data = xmltodict.parse(f.read())
        return [
            (item['nameOfIssuer'], float(item['value']))
            for item in data['informationTable']['infoTable']
        ]

    def _create_holdings_table(self, positions: list) -> Table:
        table = Table(title="Top 13F Holdings")
        table.add_column("Company", style="cyan")
        table.add_column("Value (USD)", style="magenta")
        
        for name, value in positions:
            table.add_row(name, f"${value/1e6:,.1f}M")
        return table