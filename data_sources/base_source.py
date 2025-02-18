# data_sources/base_source.py
from abc import ABC, abstractmethod
from config.core import Config
import pandas as pd
import pickle
import hashlib
import time

class FinancialDataSource(ABC):
    def __init__(self, source_name):
        self.source_name = source_name
        self.cache_enabled = True
        
    @abstractmethod
    def _fetch_data(self, ticker, **params):
        pass
        
    def get_data(self, ticker, cache_key=None, **params):
        if self.cache_enabled:
            data = self._check_cache(ticker, cache_key, params)
            if data is not None:
                return data
                
        fresh_data = self._fetch_data(ticker, **params)
        self._store_cache(ticker, cache_key, params, fresh_data)
        return fresh_data
        
    def _cache_key(self, ticker, params):
        param_str = str(sorted(params.items())).encode()
        return hashlib.md5(f"{ticker}-{param_str}".encode()).hexdigest()
        
    def _check_cache(self, ticker, cache_key, params):
        cache_file = Config.CACHE_DIR / f"{self.source_name}_{cache_key or self._cache_key(ticker, params)}.pkl"
        if cache_file.exists():
            if time.time() - cache_file.stat().st_mtime < Config.CACHE_TTL:
                return pickle.loads(cache_file.read_bytes())
        return None
        
    def _store_cache(self, ticker, cache_key, params, data):
        cache_file = Config.CACHE_DIR / f"{self.source_name}_{cache_key or self._cache_key(ticker, params)}.pkl"
        cache_file.write_bytes(pickle.dumps(data))