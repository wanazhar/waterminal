# technical/vwap.py
import pandas as pd
from rich.table import Table
from typing import Dict

class VolumeWeightedAverage:
    @staticmethod
    def calculate(data):
        vwap = (data['Close'] * data['Volume']).cumsum() / data['Volume'].cumsum()
        return vwap.rename('VWAP')