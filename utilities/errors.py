# utilities/errors.py
from rich.console import Console
import logging

console = Console()
logger = logging.getLogger("waterminal")

class WaterminalError(Exception):
    """Base exception class"""

class DataSourceError(WaterminalError):
    """Data source failure"""

class ValidationError(WaterminalError):
    """Data validation failure"""

def handle_error(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except WaterminalError as e:
            console.print(f"[red]Error: {str(e)}[/]")
            logger.error(str(e))
        except Exception as e:
            console.print(f"[bold red]Critical Error: {str(e)}[/]")
            logger.exception("Unexpected error occurred")
    return wrapper