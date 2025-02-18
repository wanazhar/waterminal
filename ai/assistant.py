# ai/assistant.py
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from openrouter import AsyncOpenRouter
from config.core import Config
import asyncio

class AIAssistant:
    def __init__(self):
        self.console = Console()
        self.client = AsyncOpenRouter(
            api_key=Config.API_KEYS['openrouter'],
            base_url="https://openrouter.ai/api/v1"
        )
        self.chat_history = []
        
    async def chat_session(self):
        self.console.print("\n[bold cyan]💻 AI Financial Assistant[/] (type 'exit' to quit)")
        while True:
            try:
                prompt = await self._get_input()
                if prompt.lower() == 'exit':
                    break
                    
                with Live(console=self.console, refresh_per_second=4) as live:
                    response = await self._stream_response(prompt)
                    live.update(Markdown(response))
                    
                self._update_history(prompt, response)
                
            except Exception as e:
                self.console.print(f"[red]Error: {str(e)}[/]")

    async def _get_input(self):
        return await asyncio.to_thread(
            self.console.input, "[bold yellow]➤ Your question: [/]"
        )

    async def _stream_response(self, prompt):
        full_response = ""
        async for chunk in self.client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[{
                "role": "user",
                "content": f"Act as a financial analyst. Be concise. Use markdown. {prompt}"
            }],
            stream=True
        ):
            delta = chunk.choices[0].delta.content or ""
            full_response += delta
            yield Markdown(full_response)
            
    def _update_history(self, prompt, response):
        self.chat_history.append({
            "prompt": prompt,
            "response": response,
            "timestamp": datetime.now().isoformat()
        })