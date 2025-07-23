from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26504251"
# -------------------------------------------------------------
API_HASH = "a50070614b2e87e3a0f2cd3ae08034c9"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "8130271170"))
SUPPORT_GRP = "ARISHFA_UPDATE"
UPDATE_CHNL = "THUNDERDEVS"
OWNER_USERNAME = "System0999"
