# hedge_funds/replication.py
from sec_edgar_downloader import Downloader
from rich.table import Table
import xmltodict
import os

class HedgeFundReplicator:
    @staticmethod
    def top_holdings(cik):
        positions = HedgeFundTracker().get_latest_13f(cik)
        return sorted(positions.items(), key=lambda x: x[1], reverse=True)[:10]