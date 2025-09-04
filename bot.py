import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import MessageEntityMentionName

# Your Telegram API credentials (get from https://my.telegram.org)
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

# Create the Telegram client (userbot)
client = TelegramClient('userbot_session', api_id, api_hash)

@client.on(events.NewMessage(pattern='@everyone'))
async def handler(event):
    chat = await event.get_chat()
    # Fetch all participants in the chat
    participants = await client.get_participants(chat)

    # Prepare the message with mentions in batches of up to 50
    mention_text = ''
    batch_size = 50
    entities = []
    start = 0

    for i, user in enumerate(participants):
        mention = f'[{user.first_name}](tg://user?id={user.id}) '
        mention_text += mention
        if (i + 1) % batch_size == 0 or (i + 1) == len(participants):
            # Send message and reset
            await event.respond(mention_text, parse_mode='md', link_preview=False)
            mention_text = ''

async def main():
    print("Userbot is running...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
