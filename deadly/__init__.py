import asyncio
import logging
import sys
import time
from aiohttp import ClientSession

from deadly.Clients import *
from deadly.methods import *
from deadly.pyrogram import ShicyMethods
from deadly.pyrogram import eod, eor
from deadly.utils import GenSession
from deadly.telethon.deadly import *


# starting logging:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("deadly").setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pyrogram.client").setLevel(logging.ERROR)
logging.getLogger("pyrogram.session.auth").setLevel(logging.ERROR)
logging.getLogger("pyrogram.session.session").setLevel(logging.ERROR)


logs = logging.getLogger(__name__)


__copyright__ = "Copyright (C) 2023-present DeadlyUserbot <https://github.com/Team-Deadly/DeadlyUserbot>"
__license__ = "GNU General Public License v3.0 (GPL-3.0)"
__version__ = "0.1.7"
deadly_ver= "0.0.5"


adB = MongoDB()

DEVS = [
    5937170640 # Blaze
]

StartTime = time.time()


class PyrogramCLI(deadlyMethods, GenSession, Methods):
    pass


class TelethonCLI(deadlyMethod, GenSession, Methods):
    pass


creds_msg = (f"Powered By @Team-Deadly ☠") 

fail_msg = (f"""
========================×========================
    Really Stupid Commit So There's No Error   
           Credit DeadlyUserbot {__version__}
========================×========================
"""
)

start_bot = (f"""
========================×========================
         Starting DeadlyUserbot [🇮🇳] Version {deadly_ver}
        Copyright (C) 2023-present DeadlyUserbot
========================×========================
"""
)

run_as_module = False

if sys.argv[0] == "-m":
    run_as_module = True

    from .decorator import *

    print("\n\n" + __copyright__ + "\n" + __license__)
    print(start_bot)

    update_envs()

    CMD_HELP = {}
    adB = MongoDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
    vc = VcTools()
else:
    print(creds_msg)
    print("\n\n" + __copyright__ + "\n" + __license__)
    print(fail_msg)

    adB = MongoDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
