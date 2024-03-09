from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response_from_ocr, replaycodes_to_string, load_templates

# load token safely
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")


# setup bot
intents: Intents = Intents.default()
intents.message_content = True 
intents.messages = True
client: Client = Client(intents=intents)
# load templates into memory when bot is launched
list_of_templates = load_templates()

# message functionality
async def respond_to_message(message: Message) -> None:
    try:
        if message.attachments:
            for attachment in message.attachments:
                #print(attachment.filename.lower())
                # accept any image except for gif
                media_type = attachment.content_type.lower().split("/")
                if media_type[0] == "image" and not media_type[1] == "gif":
                    if attachment.url:
                        # load image
                        image_data = await attachment.read()
                        # validate image?
                        
                        # tell user image is being processed
                        message_to_channel = await message.channel.send("Processing input...")
                        # process image
                        response: [str] = await get_response_from_ocr(image_data, list_of_templates)
                        #message_text = replaycodes_to_string(response)
                        # await message.channel.send(message_text)
                        #await message_to_channel.edit(content=message_text)
                        await message_to_channel.edit(content=response)
                        # reactions ToDO
                        # 400 Bad Request (error code: 50035): Invalid Form Body
                        # replaycode-ocr  | In emoji_id: Value "" is not snowflake.
                        #await message_to_channel.add_reaction(":white_check_mark:")
                        #await message_to_channel.add_reaction(":cross_mark:")
                        # log for testing
                        print(f"[{message.guild} - {message.channel}] {message.author}: {attachment.url}")
                        print(response)
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