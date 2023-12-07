import os

API_ID = API_ID = 20463500

API_HASH = os.environ.get("API_HASH", "5db9bc6439f7b43daa75689edf65b431")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6975682316:AAHd_Sr7H4PA97GzpHp-Qg2UMxNb4o3UF0g")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6981453498))

LOG = -1002008774612

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6333211826").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


