# utilities/setup_wizard.py
from rich.console import Console
from rich.panel import Panel
from config.core import Config
import os

console = Console()

def first_time_setup():
    console.print(Panel.fit("[bold green]🚀 Welcome to Waterminal Setup Wizard\n[/]"))
    
    # API Keys Configuration
    api_keys = {
        'alpha_vantage': console.input("[bold]Enter Alpha Vantage API Key: [/]"),
        'openrouter': console.input("[bold]Enter OpenRouter API Key: [/]"),
        'fred': console.input("[bold]Enter FRED API Key: [/]")
    }
    
    # Write to .env
    with open('.env', 'w') as f:
        for k,v in api_keys.items():
            f.write(f'{k.upper()}_KEY={v}\n')
    
    console.print("[green]✓ Configuration saved successfully![/]")