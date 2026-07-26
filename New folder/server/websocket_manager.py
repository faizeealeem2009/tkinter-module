from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.active_users = {}

    async def connect(
        self,
        username,
        websocket: WebSocket
    ):
        await websocket.accept()

        self.active_users[username] = websocket

    def disconnect(self, username):

        if username in self.active_users:
            del self.active_users[username]

    async def send_private_message(
        self,
        sender,
        receiver,
        message
    ):

        if receiver in self.active_users:

            await self.active_users[
                receiver
            ].send_json({
                "sender": sender,
                "message": message
            })


manager = ConnectionManager()