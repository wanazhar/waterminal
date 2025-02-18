# config/core.py
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).parent.parent
load_dotenv(BASE_DIR / ".env")

class Config:
    API_KEYS = {
        'alpha_vantage': os.getenv('ALPHA_VANTAGE_KEY'),
        'openrouter': os.getenv('OPENROUTER_KEY'),
        'eodhd': os.getenv('EODHD_KEY')
    }
    
    CACHE_DIR = BASE_DIR / ".cache"
    CACHE_TTL = 3600  # 1 hour
    
    @classmethod
    def validate(cls):
        cls.CACHE_DIR.mkdir(exist_ok=True)
        return all(cls.API_KEYS.values())