# utilities/cache.py
import functools
from config.core import Config
import diskcache
import hashlib

cache = diskcache.Cache(Config.CACHE_DIR / "advanced_cache")

def smart_cache(ttl=3600, key_fn=None):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = key_fn(*args, **kwargs) if key_fn else _generate_key(func, *args, **kwargs)
            
            if result := cache.get(cache_key):
                return result
                
            result = await func(*args, **kwargs)
            cache.set(cache_key, result, expire=ttl)
            return result
        return wrapper
    return decorator

def _generate_key(func, *args, **kwargs):
    args_repr = repr(args)
    kwargs_repr = repr(sorted(kwargs.items()))
    return hashlib.md5(f"{func.__name__}-{args_repr}-{kwargs_repr}".encode()).hexdigest()