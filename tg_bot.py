from telethon import TelegramClient
from telethon.tl.types import PeerChat, PeerChannel
from telethon import utils
import math
from datetime import datetime, timezone

# Remember to use your own values from my.telegram.org!
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    #print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    #print(username)
    #print(me.phone)
    print("""
    ##########################
    ####### NEW RUN ##########
    ##########################
        """)

    # You can print all the dialogs/conversations that you are part of:
    chat_id = None
    await client.get_dialogs()
    async for dialog in client.iter_dialogs():
        if dialog.name == "delete test group":
            chat_id = dialog.id
    real_id, peer_type = utils.resolve_id(chat_id)
    my_chat    = await client.get_entity(PeerChat(real_id))
    async for messages in client.iter_messages(my_chat):
            if "MessageActionChatAddUser" in str(messages.action) or "MessageActionChatJoinedByLink" in str(messages.action):
                if messages.date >= datetime(2021, 8, 30, 21, 20, 0, tzinfo=timezone.utc) and messages.date <= datetime(2021, 9, 1, 11, 29, 0, tzinfo=timezone.utc):
                    for user in messages.action.users:
                        msg = await client.kick_participant(my_chat, user)
                        await msg.delete()
with client:
    client.loop.run_until_complete(main())
