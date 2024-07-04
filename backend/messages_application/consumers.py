from random import choice
from string import digits
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
  async def connect(self):
    await self.accept()
    request_user = self.scope['user']

    if request_user.is_anonymous:
      identifier = "".join(choice(digits) for _ in range(4))
      self.partial_user = { 
        'id': None, 
        'username': f'anonymous#{identifier}' 
      }
    
    else:
      self.partial_user = { 
        'id': request_user.id, 
        'username': request_user.username 
      }
  
  async def disconnect(self, code):
    pass

  async def receive_json(self, content, **kwargs):
    message = content['message']
    
    if not len(message) > 1000:
      await self.send_json({ 
        'user': self.partial_user, 
        'message': message 
      })


class HealthCheckConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept(); await self.send('Connected!')
  
  async def disconnect(self, code):
    pass
