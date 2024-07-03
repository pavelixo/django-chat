import json
from channels.generic.websocket import AsyncWebsocketConsumer


class HealthCheckConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept(); await self.send('Connected!')
  
  async def disconnect(self, code):
    pass