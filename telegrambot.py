from telethon.sync import TelegramClient, events
from dotenv import dotenv_values
from telethon.tl.functions.channels import GetFullChannelRequest

import database
import dexscreener
import eth

# Load the API credentials and phone number from the .env file
config = dotenv_values(".env")
api_id = config["API_ID"]
api_hash = config["API_HASH"]
phone_number = config["PHONE_NUMBER"]
session_file = 'session_name.session'

# Create a TelegramClient instance
client = TelegramClient(session_file, api_id, api_hash)

# Start the client
client.start(phone_number)


# Event handler for new messages
@client.on(events.NewMessage(incoming=True, forwards=False))
async def handle_new_message(event):
    # Get the channel information
    sender = await event.get_sender()
    entity = await client(GetFullChannelRequest(event.chat_id))
    channel_title = entity.chats[0].title
    print(event.message.text)
    token = eth.extract_token(event.message.text)
    if token:
        token_stats = dexscreener.get_token_info(token)
        print(channel_title, token_stats)
        database.add(token_stats, channel_title)



# Run the client until the program is terminated
client.run_until_disconnected()
