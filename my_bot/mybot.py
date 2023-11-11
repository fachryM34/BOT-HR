import asyncio
from highrise import BaseBot
from highrise.models import SessionMetadata, User
from highrise import __main__  
from asyncio import run as arun 

class Bot(BaseBot):
        async def on_start(self, session_metadata: SessionMetadata):
                print("Am I Alive")

        async def on_user_join(self, user: User) -> None:
                print(f"{user.username} has joined the room.")
                await self.highrise.chat(f"WB, {user.username}")

        async def on_chat(self, user, message: str):
                print(f"{user.username} said: {message}")

        async def run(self, room_id, token):
                await __main__.main(self, room_id, token)

if __name__ == "__main__":
    room_id = "652053f4dccb2d2013c1727b"
    token = "15bcbc31693e0407b97ca032c90dcc8abcafacdc72f939b0b6be7233a262d76b"
    arun(Bot().run(room_id, token))


