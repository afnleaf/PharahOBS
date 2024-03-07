from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response_from_ocr, replaycodes_to_string

# load token safely
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")


# setup bot
intents: Intents = Intents.default()
intents.message_content = True 
intents.messages = True
client: Client = Client(intents=intents)


# message functionality
async def respond_to_message(message: Message) -> None:
    try:
        if message.attachments:
            for attachment in message.attachments:
                if attachment.url:
                    image_data = await attachment.read()
                    response: [str] = await get_response_from_ocr(image_data)
                    message_text = replaycodes_to_string(response)
                    await message.channel.send(message_text)
    except Exception as e:
        print(e)


# handle startup of bot
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running.")


# handle incoming messages
@client.event
async def on_message(message: Message) -> None:
    # ignore self
    if message.author == client.user:
        return
    # channel setup to make sure bot only monitors channel with vods
    # check what channel message is in

    #username: str = str(message.author)
    #user_message: str = message.content
    #channel: str = str(message.channel)
    #attachments = message.attachments
    #print(f"[{channel}] {username}: \"{user_message}\"")
    #await send_message(message, user_message, attachments)
    await respond_to_message(message)


# main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()