import os

from dotenv import load_dotenv

load_dotenv()

ROOT_PATH = os.getenv("ROOT_PATH", "/api")
HOST = os.getenv("HOST", "http://localhost:8000")

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_REDIRECT_URI = HOST + ROOT_PATH + "/auth/github"

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = HOST + ROOT_PATH + "/auth/google"

MICROSOFT_CLIENT_ID = os.getenv("MICROSOFT_CLIENT_ID")
MICROSOFT_CLIENT_SECRET = os.getenv("MICROSOFT_CLIENT_SECRET")
MICROSOFT_REDIRECT_URI = HOST + ROOT_PATH + "/auth/microsoft"
