# data_sources/alpha_vantage/historical.py
from data_sources.base_source import FinancialDataSource
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

class AlphaVantageHistorical(FinancialDataSource):
    def __init__(self):
        super().__init__("alpha_vantage")
        self.ts = TimeSeries(
            key=Config.API_KEYS['alpha_vantage'],
            output_format='pandas',
            indexing_type='date'
        )
        
    def _fetch_data(self, ticker, interval='daily', output_size='compact'):
        func_map = {
            'daily': self.ts.get_daily,
            'intraday': self.ts.get_intraday
        }
        data, meta = func_map[interval](
            symbol=ticker,
            outputsize=output_size
        )
        return self._standardize_format(data)
        
    def _standardize_format(self, df):
        return df.rename(columns={
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        })