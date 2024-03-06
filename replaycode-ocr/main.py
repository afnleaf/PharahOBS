from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response, replaycodes_to_string

# load token safely
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# setup bot
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)


# message functionality
async def send_message(message: Message, user_message: str, attachments) -> None:
    try:
        for attachment in attachments:
            print(attachment.url)
            # fetch image
            if attachment.url:
                #response: str = await get_response(attachment.url)
                image_data = await attachment.read()
                response: [str] = await get_response(image_data)
                message_text = replaycodes_to_string(response)
                await message.channel.send(message_text)
    except Exception as e:
        print(e)

    #if not user_message:
    #    print("(Message was empty, intents not enabled)")
    #    #return
    # is_private = user_message[0] == ? return true or false
    #if is_private := user_message[0] == "?":
    #    user_message = user_message[1:]
    #await message.author.send(response) if is_private else await message.channel.send(response)


# handle startup of bot
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running.")

# handle incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    attachments = message.attachments

    print(f"[{channel}] {username}: \"{user_message}\"")
    await send_message(message, user_message, attachments)


# main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()