# data_sources/source_router.py
from importlib import import_module
from config.core import Config

SOURCES_CONFIG = {
    'historical': [
        ('alpha_vantage', 'AlphaVantageHistorical'),
        ('yfinance', 'YFinanceHistorical')
    ],
    'fundamentals': [
        ('eodhd', 'EODHDFundamentals'),
        ('yfinance', 'YFinanceFundamentals')
    ]
}

def get_data(ticker, data_type, **params):
    for source, class_name in SOURCES_CONFIG.get(data_type, []):
        try:
            module = import_module(f"data_sources.{source}.{data_type}")
            source_class = getattr(module, class_name)()
            return source_class.get_data(ticker, **params)
        except Exception as e:
            continue
    raise ValueError(f"No available source for {data_type} data")