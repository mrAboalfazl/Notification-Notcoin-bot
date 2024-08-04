from telethon import TelegramClient, events
from config import API_ID, API_HASH
from telethon.tl.custom.message import Message
from telethon import Button

client = TelegramClient("Notcoin Notification", API_ID, API_HASH)


@client.on(events.NewMessage(pattern=r'/start'))
async def start(event : Message) :

    markup = client.build_reply_markup(
        [
            Button.inline("First Button"),
            Button.inline("Second Button")
        ]
    )
    await event.respond("Hey Magi", buttons= markup)

    markup = client.build_reply_markup(
        [
            Button.text("Keyboard")
        ]
    )
    await event.reply("I am good", buttons= markup)




client.start()
client.run_until_disconnected()