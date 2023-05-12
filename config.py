import os

API_ID = API_ID = 23442389

API_HASH = os.environ.get("API_HASH", "70490ec8a810932cb5cb7f9d6a839ee0")

BOT_TOKEN = os.environ.get("5936066423:AAFPDK0ZJUcCdT794im-HRcGDyCny4jPQWo")

OWNER = int(os.environ.get("OWNER", 5448647404))

LOG = -808921320

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5448647404").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

