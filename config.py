import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("26416417"))
API_HASH = os.getenv("3895a4b1872eac25b9a5ddb10b270499")
SESSION = os.getenv("BQGTFSEAV5VzwBuqLlduIpzDPfsfTKyhoCKt9cft1XK6yrHxLqjVseYAeiy5O_TEzKqniwn4n9z3Saku1ib1KC8GFtoStB06ltSC5qPm4pzaCoFbSlm4jIB5Dlm-ATDNdAtykle2J_9AL-WEIJq3BhlZre4_PFpnc3lHSTAUUmRqxtOcWNCMpSt6XUMXl55g8hteQhfBQfb-pJn7y4NQl_XoEzcecShPTvCKl3Zd2HMKRTTQ5KSg0vb_xp1wKcb8aep_OOUm3agvyb8fLvWoADIKGSqJ0eVpaNQWK4NLq_tlc0l_dIcEdyeiD-OkD4MjEMdkFJh15EM2iP0Zgepws-DSKCbytAAAAAGmOcdDAA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("7083771715").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
