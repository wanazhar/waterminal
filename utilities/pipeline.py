# utilities/pipeline.py
import aiohttp
import asyncio
from data_sources.source_router import get_data
from data_sources.datasource import DataSource
from technical_analysis import TechnicalAnalysis

class DataPipeline:
    @staticmethod
    async def fetch_concurrent(tasks):
        async with aiohttp.ClientSession() as session:
            return await asyncio.gather(*tasks)
            
    @staticmethod
    async def get_live_prices(symbols):
        tasks = [
            get_data(symbol, 'realtime', source='alpha_vantage')
            for symbol in symbols
        ]
        return await DataPipeline.fetch_concurrent(tasks)
        
    @staticmethod
    async def bulk_historical(symbols, start, end):
        tasks = [
            get_data(symbol, 'historical', start=start, end=end)
            for symbol in symbols
        ]
        return await DataPipeline.fetch_concurrent(tasks)

    @staticmethod
    async def get_technical_data(ticker):
        closes = await DataSource.get(ticker, 'daily_closes')
        return {
            'prices': closes,
            'sma20': closes.rolling(20).mean(),
            'sma50': closes.rolling(50).mean(),
            'rsi': await TechnicalAnalysis.rsi(closes)
        }