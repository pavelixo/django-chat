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

        await self.channel_layer.group_add(
            'chat_room',
            self.channel_name
        )

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            'chat_room',
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        message = content.get('message')

        if message and len(message) <= 1000:
            await self.channel_layer.group_send(
                'chat_room',
                {
                    'type': 'chat.message',
                    'user': self.partial_user,
                    'message': message
                }
            )

    async def chat_message(self, event):
        await self.send_json({
            'user': event['user'],
            'message': event['message']
        })


class HealthCheckConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept(); await self.send('Connected!')
  
  async def disconnect(self, code):
    pass
