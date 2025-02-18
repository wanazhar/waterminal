# utilities/forms.py
from rich.console import Console
from rich.prompt import Prompt
from questionary import Style, text

console = Console()

custom_style = Style([
    ('qmark', 'fg:#00ff00 bold'),
    ('question', 'fg:#00ffff bold'),
    ('answer', 'fg:#ff00ff'),
    ('instruction', 'fg:#884444 italic')
])

class TerminalForms:
    @staticmethod
    def ticker_input():
        return text(
            "Enter stock ticker:",
            validate=lambda t: len(t) <= 5 and t.isalpha(),
            style=custom_style
        ).ask()
        
    @staticmethod
    def date_range_input():
        return console.input("[bold]Enter date range (YYYY-MM-DD to YYYY-MM-DD): [/]")
        
    @staticmethod
    def ratio_selection():
        return Prompt.ask(
            "[bold cyan]Select ratio type:[/]",
            choices=["Valuation", "Profitability", "Liquidity"],
            show_choices=False
        )