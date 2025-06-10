import asyncio
import websockets

class ChatClient:
    def __init__(self, uri="wss://web-production-91c78.up.railway.app/ws"):
        self.uri = uri
        self.messages = []

    async def connect(self):
        self.websocket = await websockets.connect(self.uri)

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        while True:
            msg = await self.websocket.recv()
            self.messages.append(msg)

    async def run(self, message_to_send):
        if not hasattr(self, 'websocket'):
            await self.connect()
            asyncio.create_task(self.receive())
        if message_to_send:
            await self.send(message_to_send)
