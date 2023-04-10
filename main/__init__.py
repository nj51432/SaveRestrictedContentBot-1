#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "29829499" , cast=int)
API_HASH = config("API_HASH", "0f84221a8f1fa856e96f8b50ba4c6930")
BOT_TOKEN = config("BOT_TOKEN", "6195271217:AAGPeFPdouw-P5JlsKh9OG4PyMFtpSgrQsc")
SESSION = config("SESSION", "BQCsJap6Pa10JtVGaCnmH516mnSkULzu9o1Js7UFRkmGYX08X_u-_0R3kU4oL0crhigP4sx3jCwnS1MjZST7uiKisMe8mVtci_RZQohyg9gQmUt2H_VwMoqFp5CFXpz_VRf0-Y3cNh3FVz6DCu-RIgslY2Vpl1PCFhzxIVRm3ReL6TtcoBSjytGlmYjWyhbXMaCNsgdKekEjVdOWOh_3Ztx0JvKsA2wekCUQ6LiSEyKs22zbFWpOqjMhRIx8YBlCZUtzMOlpIi-kEwnPh8uynMTkxKI7A_NnkqDrPfRRzXg-RG7GWsp5sWjzJbrA7FcZy0mV-JO-ZZsLSkLNyMe6eyRKZrlUEgA")
FORCESUB = config("FORCESUB", "nj")
AUTH = config("AUTH", "1001907318415", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
