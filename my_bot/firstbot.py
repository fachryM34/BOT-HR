from highrise import BaseBot
from highrise.models import SessionMetadata, User
from highrise import __main__
from asyncio import run as arun

# Bot is our version of highrise-bot-sdks BaseBot
# where we override functions like on_chat to give them more interesting functionality
class Bot(BaseBot):
  
    async def on_start(self, session_metadata: SessionMetadata):
        print("hi im alive?") # this should output in the terminal

    # this function is called every time a user sends a message in the room with the bot
    async def on_chat(self, user: User, message: str):
        # we log this message to the terminal on your machine with print
        print(f"{user.username} said: {message}")

    async def run(self, room_id, token):
        await __main__.main(self, room_id, token)

if __name__ == "__main__":
    room_id = "652053f4dccb2d2013c1727b"
    token = "15bcbc31693e0407b97ca032c90dcc8abcafacdc72f939b0b6be7233a262d76b"
    arun(Bot().run(room_id, token))
    