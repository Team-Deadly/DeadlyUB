import asyncio
import importlib
import sys

from pyrogram import idle

from deadly import __version__

from deadly import *

from deadly.config import Var
from deadly.Clients.startup import StartPyrogram
from deadly.exceptions import DependencyMissingError

Var = Var()
pdeadly = deadlyp()


try:
    from uvloop import install
except:
    install = None
    logs.info("'uvloop' not installed\ninstall 'uvloop' or add 'uvloop' in requirements.txt")


MSG_ON = """
<b>❏ Welcome to DeadlyUserbot [🇮🇳]</b>
<b>├▹ Package Version</b> - •[<code>{}</code>]•
<b>├▹ Hosting Info</b> - <code>{}</code>
<b>├▹ DeadlyUserbot Version</b> - <code>{}</code>
<b>├▹ Plugins Count</b> - <code>{}</code>
"""

async def start_main():
    await StartPyrogram()
    try:
        await tgbot.send_message(
            Var.LOG_CHAT,
            MSG_ON.format(
                __version__,
                HOSTED_ON,
                deadly_ver, 
                len(CMD_HELP),
            )
        )
    except BaseException as s:
        print(s)
    print(f"DeadlyUserbot  Version - {deadly_ver}\n⚡ Started Successfully !")
    await idle()
    await aiosession.close()

if __name__ == "__main__":
    install()
    loop.run_until_complete(start_main())
    logs.info("Stopping DeadlyUserbot! GoodBye ☠")
    
