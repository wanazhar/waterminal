# utilities/pipeline.py
import aiohttp
import asyncio
from data_sources.source_router import get_data

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