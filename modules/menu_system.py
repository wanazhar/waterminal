# modules/menu_system.py
from rich.console import Console
from rich.table import Table
from config.menu_config import MENU_STRUCTURE

class MainMenu:
    def __init__(self):
        self.console = Console()
        self.menu_stack = []
        
    def display(self):
        while True:
            current_menu = MENU_STRUCTURE if not self.menu_stack else self.menu_stack[-1]['children']
            self._render_menu(current_menu)
            choice = self.console.input("\n[bold yellow]➤ Select option: [/]")
            
            if choice.lower() == 'b':
                if self.menu_stack: self.menu_stack.pop()
                continue
                
            selected = next((item for item in current_menu if str(item['id']) == choice), None)
            
            if selected:
                if 'children' in selected:
                    self.menu_stack.append(selected)
                else:
                    self._execute_module(selected['module'])

    def _render_menu(self, items):
        table = Table(show_header=False, box=None)
        for item in items:
            table.add_row(f"[bold]{item['id']}[/]", item['label'])
        self.console.print(table)
        
    def _execute_module(self, module_path):
        # Dynamic module loading implementation
        pass