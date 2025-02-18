# utilities/display.py
from rich.console import Console
from rich.table import Table

def create_table(title, columns, rows):
    console = Console()
    table = Table(title=title)
    
    for col in columns:
        table.add_column(col)
        
    for row in rows:
        table.add_row(*[str(x) for x in row])
        
    console.print(table)