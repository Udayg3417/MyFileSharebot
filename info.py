
import re
from os import environ


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Auto Delete
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), False)
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))

# Bot Information 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "21562110"))
API_HASH = os.environ.get("API_HASH", "4d1e1f333214a39cea79a3196cbed290")
ADMINS =int(os.environ.get("ADMINS", "6909056240")
ADMINS = environ.get("ADMINS", OWNER)

#Channel 
CHANNEL = int(os.environ.get("CHANNEL", "-1002191088551"))
OWNER = int(os.environ.get("OWNER", "6909056240"))
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1001902643858"))
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

# MongoDB Database 
PORT = os.environ.get("PORT", "8080")
DATABASE_URI = os.environ.get("DATABASE_URL", "mongodb+srv://guday3417:GUDAY333@cluster0.pdrwfcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Other 
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6909056240").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")



