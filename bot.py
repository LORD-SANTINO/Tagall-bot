import os
import asyncio
from telethon import TelegramClient, events

# Load credentials from environment variables
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

client = TelegramClient('userbot_session', api_id, api_hash)

@client.on(events.NewMessage(pattern='@everyone'))
async def handler(event):
    chat = await event.get_chat()
    participants = await client.get_participants(chat)

    mention_text = ''
    batch_size = 50

    for i, user in enumerate(participants):
        mention_text += f'[{user.first_name}](tg://user?id={user.id}) '
        if (i + 1) % batch_size == 0 or (i + 1) == len(participants):
            await event.respond(mention_text, parse_mode='md', link_preview=False)
            mention_text = ''

async def main():
    print("Userbot is running...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
