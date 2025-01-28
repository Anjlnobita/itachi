import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from JioSavaan import LOGGER, app
#, userbot
#from JioSavaan.core.call import Anony
from JioSavaan.misc import sudo
from JioSavaan.plugins import ALL_MODULES
from JioSavaan.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("JioSavaan.plugins" + all_module)
    LOGGER("JioSavaan.plugins").info("Successfully Imported Modules...")
   
   
    await idle()
    await app.stop()
   # await userbot.stop()
    LOGGER("JioSavaan").info("Stopping JioSavaan Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
