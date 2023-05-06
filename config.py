from os import environ, system
from os.path import exists
from sys import exit
from logging import StreamHandler, getLogger, basicConfig, ERROR, INFO
from logging.handlers import RotatingFileHandler
from time import time
from dotenv import load_dotenv
from configparser import ConfigParser




basicConfig(
    level=INFO,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "Logging.txt", maxBytes=50000000, backupCount=10, encoding="utf-8"
        ),
        StreamHandler(),
    ],
)


getLogger("pyrogram").setLevel(ERROR)
LOGGER = getLogger()



def get_drive_name(file):
    try:
        config = ConfigParser(default_section=False)
        config.read(file, encoding="utf-8")
        accounts = []
        for d in config:
            if d:
                accounts.append(str(d))
        if len(accounts):
            LOGGER.info(f"🔶Selecting {accounts[0]} As Upload Drive")
            return accounts[0]
        else:
            LOGGER.info(f"❌No Drive Found IN Rclone Config")
            exit()
    except Exception as e:
        LOGGER.info(f"❌Error Getting Drive Name From Rclone Config: {str(e)}")
        exit()


if exists('config.env'):
        LOGGER.info(f"🔶Importing Config File")
        load_dotenv('config.env')

RCLONE_CONFIG_FILE = environ.get("RCLONE_CONFIG_FILE", False)
if RCLONE_CONFIG_FILE:
    LOGGER.info(f"🔶Downloading Rclone Config File")
    system(f"wget -q '{RCLONE_CONFIG_FILE}' -O ./rclone.conf")
else:
    LOGGER.error("❌Rclone Config File Variable Not Found")
    exit()


if not exists("rclone.conf"):
    LOGGER.error("❌Rclone Config File Not Found")
    exit()


DRIVE_NAME = environ.get("DRIVE_NAME", False)

if not DRIVE_NAME:
    LOGGER.info(f"🔶DRIVE NAME not found in config")
    DRIVE_NAME = get_drive_name("rclone.conf")


class Config:
    botStartTime = time()
    LOGGER = LOGGER
    API_ID = int(environ.get("API_ID",""))
    API_HASH = environ.get("API_HASH","")
    BOT_TOKEN = environ.get("BOT_TOKEN","")
    DRIVE_NAME = DRIVE_NAME
    STATUS_UPDATE_TIME = int(environ.get("STATUS_UPDATE_TIME","7"))
    FINISHED_PROGRESS_STR = environ.get("FINISHED_PROGRESS_STR", '■')
    UNFINISHED_PROGRESS_STR = environ.get("UNFINISHED_PROGRESS_STR", '□')
    DRIVE_BASE_DIR = environ.get("DRIVE_BASE_DIR","Mega_Downloader")
    DOWNLOAD_PATH = environ.get("DOWNLOAD_PATH","./downloads")
    LOGS_PATH = environ.get("LOGS_PATH","./logs")

