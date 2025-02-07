import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import ChatUser

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Añadimos al usuario al grupo de chat
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )

        # Enviamos notificación de usuario conectado
        user_name = self.scope.get('user', None).username #Obtener el nombre del usuario
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_joined',
                'message': f'{user_name} se ha unido al chat'
            }
        )

        # Confirmamos que la conexion ha sido aceptada
        await self.accept()

    async def disconnect(self, close_code):
        # Enviamos la notificacion de usuario desconectado
        user_name = self.scope.get('user', None).username #Obtener el nombre del usuario
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_left',
                'message': f'{user_name} ha salido del chat'
            }
        )

        #Quitamos al usuario del group
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
        )

    # Recibir mensaje de WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Enviar mensaje al grupo de chat
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                'type': 'chat.message', 
                'message': message
            }
        )

    # Recibir mensaje de grupo
    async def chat_message(self, event):
        message = event['message']

        # Enviar mensaje a WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    # Notificación de usuario conectado
    async def user_joined(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'system_message': message
        }))

    # Notificación de usuario desconectado
    async def user_left(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'system_message': message
        }))