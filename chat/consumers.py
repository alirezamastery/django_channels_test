import json

from channels.generic.websocket import WebsocketConsumer
from channels.auth import UserLazyObject


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope.get('user', None)
        print(f'user: {type(self.user)}')
        if self.user:
            print(self.user)
        if self.user and not isinstance(self.user, UserLazyObject):
            self.accept()

    def disconnect(self, close_code):
        print('ggggg')

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
