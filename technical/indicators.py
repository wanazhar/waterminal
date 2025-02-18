# technical/indicators.py
import pandas_ta as ta
from rich.table import Table

class TechnicalAnalyzer:
    @staticmethod
    def calculate_rsi(data, window=14):
        return ta.rsi(data['Close'], length=window)
        
    @staticmethod
    def moving_average_crossover(data, short=50, long=200):
        return pd.DataFrame({
            'MA50': ta.sma(data['Close'], length=short),
            'MA200': ta.sma(data['Close'], length=long)
        })
        
    @staticmethod
    def macd(data):
        return ta.macd(data['Close'])
        
    @staticmethod
    def bollinger_bands(data, window=20):
        return ta.bbands(data['Close'], length=window)