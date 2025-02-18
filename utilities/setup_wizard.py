# utilities/setup_wizard.py
from rich.prompt import Prompt
from rich.console import Console
from pathlib import Path
import json

console = Console()

def first_time_setup():
    console.print("[bold yellow]🚀 Welcome to Waterminal Setup[/]")
    keys = {
        'alpha_vantage': Prompt.ask("Enter Alpha Vantage API key"),
        'fred': Prompt.ask("Enter FRED API key"),
        'openrouter': Prompt.ask("Enter OpenRouter API key")
    }
    
    config = {
        'cache_dir': str(Path.home() / ".waterminal_cache"),
        'default_source': 'yfinance',
        'refresh_interval': 60
    }
    
    env_path = Path(".env")
    env_path.write_text("\n".join([f"{k.upper()}={v}" for k,v in keys.items()]))
    
    console.print("[bold green]✓ Setup completed![/]")