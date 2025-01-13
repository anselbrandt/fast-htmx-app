from urllib.parse import urlencode
import base64
import os
from pathlib import Path
import secrets

from dotenv import load_dotenv

load_dotenv()

base64_secret = base64.standard_b64encode(secrets.token_bytes(32)).decode("utf-8")

UPLOAD_DIR = Path() / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ENV_MODE = os.getenv("ENV_MODE", "DEV")
ROOT_PATH = os.getenv("ROOT_PATH", "")
HOST = os.getenv("HOST", "http://localhost:8000")

COOKIE_NAME = os.getenv("COOKIE_NAME", "cookie")
TOKEN_SECRET = os.getenv("TOKEN_SECRET", base64_secret)
TOKEN_ALGORITHM = "HS256"

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_REDIRECT_URI = HOST + ROOT_PATH + "/auth/github"
GITHUB_OAUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_URL = "https://api.github.com/user"
GITHUB_USER_EMAIL_URL = "https://api.github.com/user/emails"

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = HOST + ROOT_PATH + "/auth/google"
GOOGLE_OAUTH_URL = "https://accounts.google.com/o/oauth2/auth"
GOOGLE_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
GOOGLE_USER_URL = "https://www.googleapis.com/oauth2/v1/userinfo"

MICROSOFT_CLIENT_ID = os.getenv("MICROSOFT_CLIENT_ID")
MICROSOFT_CLIENT_SECRET = os.getenv("MICROSOFT_CLIENT_SECRET")
MICROSOFT_REDIRECT_URI = HOST + ROOT_PATH + "/auth/microsoft"
MICROSOFT_OAUTH_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
MICROSOFT_TOKEN_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
MICROSOFT_USER_URL = "https://graph.microsoft.com/v1.0/me"

githubParams = {
    "client_id": GITHUB_CLIENT_ID,
    "redirect_uri": GITHUB_REDIRECT_URI,
    "scope": "user:email",
}
GITHUB_LOGIN_LINK = f"{GITHUB_OAUTH_URL}?{urlencode(githubParams)}"

googleParams = {
    "response_type": "code",
    "client_id": GOOGLE_CLIENT_ID,
    "redirect_uri": GOOGLE_REDIRECT_URI,
    "scope": "openid profile email",
    "access_type": "offline",
}
GOOGLE_LOGIN_LINK = f"{GOOGLE_OAUTH_URL}?{urlencode(googleParams)}"

microsoftParams = {
    "client_id": MICROSOFT_CLIENT_ID,
    "response_type": "code",
    "redirect_uri": MICROSOFT_REDIRECT_URI,
    "response_mode": "query",
    "scope": "https://graph.microsoft.com/user.read",
}
MICROSOFT_LOGIN_LINK = f"{MICROSOFT_OAUTH_URL}?{urlencode(microsoftParams)}"
