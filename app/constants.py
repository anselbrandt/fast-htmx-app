import os

from dotenv import load_dotenv

load_dotenv()

ROOT_PATH = os.getenv("ROOT_PATH", "/api")
HOST = os.getenv("HOST", "http://localhost:8000")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = HOST + ROOT_PATH + "/auth/google"
