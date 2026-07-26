from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from auth import register_user
from auth import login_user

from websocket_manager import manager

app = FastAPI()


@app.get("/")
def root():
    return {
        "app": "ChatHub Server",
        "status": "running"
    }


@app.post("/signup")
def signup(data: dict):

    success = register_user(
        data["username"],
        data["email"],
        data["password"]
    )

    return {
        "success": success
    }


@app.post("/login")
def login(data: dict):

    success = login_user(
        data["username"],
        data["password"]
    )

    return {
        "success": success
    }


@app.websocket("/ws/{username}")
async def websocket_endpoint(
    websocket: WebSocket,
    username: str
):

    await manager.connect(
        username,
        websocket
    )

    try:

        while True:

            data = await websocket.receive_json()

            receiver = data["receiver"]
            message = data["message"]

            await manager.send_private_message(
                sender=username,
                receiver=receiver,
                message=message
            )

    except WebSocketDisconnect:

        manager.disconnect(username)