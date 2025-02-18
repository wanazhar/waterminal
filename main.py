# main.py
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from modules.menu_system import MainMenu

console = Console()

BANNER = """
██╗    ██╗ █████╗ ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
"""

def main():
    console.clear()
    console.print(Panel.fit(Markdown(BANNER), style="bold cyan")
    MainMenu().display()

if __name__ == "__main__":
    main()