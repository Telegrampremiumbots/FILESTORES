#(©)CodeXBotz



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6315736663:AAF3zP_HbbA6DvTiOW3fBvvzDCWCkTjdXas")

W#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21598475"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cb33c89838ef0b57c1b7660dc2ea5dae")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001814971168"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5606394891"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://vitibo3698:srikar123@cluster0.62a7skh.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\n 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗜𝗦 𝗢𝗪𝗡𝗘𝗗 𝗕𝗬 𝗦𝗥𝗠_𝗧𝗘𝗟𝗘_𝗠𝗜𝗫\n\n 𝗠𝗔𝗜𝗡𝗧𝗔𝗜𝗡𝗘𝗗 𝗕𝗬 @SK_INDIA")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5606394891").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝗕𝗛𝗔𝗜 𝗜 𝗔𝗠 𝗢𝗡𝗟𝗬 𝗔 𝗕𝗢𝗧 𝗝𝗢𝗜𝗡 @SRMkMiX 𝗝𝗢𝗜𝗡 𝗔𝗡𝗗 𝗪𝗔𝗧𝗖𝗛 𝗞𝗗𝗥𝗔𝗠𝗔𝗦"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
