import pandas as pd
import numpy as np

class MACDAnalyzer:
    def __init__(self, fast=12, slow=26, signal=9):
        self.fast_period = fast
        self.slow_period = slow
        self.signal_period = signal

    def calculate(self, close_prices):
        ema_fast = close_prices.ewm(span=self.fast_period, adjust=False).mean()
        ema_slow = close_prices.ewm(span=self.slow_period, adjust=False).mean()
        macd = ema_fast - ema_slow
        signal = macd.ewm(span=self.signal_period, adjust=False).mean()
        return pd.DataFrame({
            'MACD': macd,
            'Signal': signal,
            'Histogram': macd - signal
        })
