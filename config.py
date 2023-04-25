import os

API_ID = API_ID = 29410389

API_HASH = os.environ.get("API_HASH", "0c716764715886f6641477ffbb63e1ee")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5924735820:AAGDPiM3DuYmkXEGUNpsoWQxPd3qrcep4Qg")

OWNER = int(os.environ.get("OWNER", 5917311887))

LOG = -1001936874635

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5917311887").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

