# market/live_ticker.py
import websockets
import asyncio
from rich.console import Console
from rich.table import Table
from config.core import Config

class LiveTicker:
    def __init__(self):
        self.console = Console()
        self.ws_connections = {}
        self.symbols = []
        
    async def connect(self, symbols):
        self.symbols = symbols
        async with websockets.connect(Config.WS_ENDPOINT) as ws:
            await ws.send('{"type":"subscribe","symbols":%s}' % symbols)
            await self._display_loop(ws)

    async def _display_loop(self, ws):
        table = Table(title="Live Market Data", show_lines=True)
        table.add_column("Symbol", style="cyan")
        table.add_column("Price", style="magenta")
        table.add_column("Change %", style="green")
        table.add_column("Volume")
        
        with self.console.status("[bold green]Tracking live prices..."):
            async for msg in ws:
                data = self._parse_message(msg)
                self._update_table(table, data)
                self.console.clear()
                self.console.print(table)

    def _parse_message(self, msg):
        # Implement protocol-specific parsing
        return json.loads(msg)

    def _update_table(self, table, data):
        # Clear and rebuild table rows
        table.rows.clear()
        for item in data:
            table.add_row(
                item['symbol'],
                f"${item['price']:.2f}",
                f"{item['change_pct']:.2f}%",
                f"{item['volume']/1e6:.1f}M"
            )