import os

from dotenv import load_dotenv

load_dotenv() 

# Load from env
BOT_NAME = os.environ["BOT_NAME"]
OUTLOOK = os.environ["OUTLOOK"]
OUTLOOK_PWD = os.environ["OUTLOOK_PWD"]
GMAIL = os.environ["GMAIL"]
GMAIL_PWD = os.environ["GMAIL_PWD"]

# Reference URLs
TEAMS_URL = 'https://teams.microsoft.com/_#/calendarv2'
ZOOMS_URL = 'https://zoom.us/'
GOOGLE_URL = 'https://accounts.google.com'
OUTLOOK_LOGIN_URL = 'https://login.microsoftonline.com/'
WEBSOCKET_URL = "ws://localhost:7000"

TEAMS_MEETING_LINK = 'https://teams.live.com/meet/932011034979?p=fRClkxbrCli8WyFIhc'
ZOOM_MEETING_LINK = 'https://us05web.zoom.us/j/88026741587?pwd=BXSeQxSbG900nSrlEfzo89b0yoRaAk.1'
GOOGLE_MEETING_LINK = 'https://meet.google.com/iez-ezsk-ikq'

RMTP_SERVER_URL = "rtmp://rtmp-live-ingest-us-east-1-universe.dacast.com/transmuxv1"
# Keys

STREAM_KEY = "59e6e0f8-ac9a-d328-6ff6-dd4e9998f834?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHJlYW1JZCI6IjU5ZTZlMGY4LWFjOWEtZDMyOC02ZmY2LWRkNGU5OTk4ZjgzNCIsInR5cGUiOiJwdWJsaXNoIn0.bljB-Pzrr9LfcIxxhzvymNqtfRUykgNjkxbLEapE5m0"
# Logging flags
INFO = 1
ERROR = 0

# File paths
# CHROME_DRIVER_PATH = r'chromedriver.exe'
# CONFIG_FILE_PATH = r'./config.json'
