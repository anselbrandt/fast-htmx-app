from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
import httpx

from app.constants import (
    GITHUB_CLIENT_ID,
    GITHUB_CLIENT_SECRET,
    GITHUB_REDIRECT_URI,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    GOOGLE_REDIRECT_URI,
    MICROSOFT_CLIENT_ID,
    MICROSOFT_CLIENT_SECRET,
    MICROSOFT_REDIRECT_URI,
)
from app.schemas import GithubUser, GoogleUser, MicrosoftUser, Provider, User

router = APIRouter(prefix="/auth")

templates = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/github")
async def auth_github(code: str):
    token_url = "https://github.com/login/oauth/access_token"
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
        "redirect_uri": GITHUB_REDIRECT_URI,
    }
    headers = {"Accept": "application/json"}
    token_response = httpx.post(token_url, params=params, headers=headers)
    access_token = token_response.json().get("access_token")
    user_response = httpx.get(
        "https://api.github.com/user",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_response.json()
    if user_info["email"] is None:
        email_response = httpx.get(
            "https://api.github.com/user/emails",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        emails = email_response.json()
        merged = {**user_info, "email": emails[0]["email"]}
        return GithubUser.model_validate((merged))
    else:
        return GithubUser.model_validate_json(user_info)


@router.get("/google")
async def auth_google(code: str):
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_response = httpx.post(token_url, data=data)
    access_token = token_response.json().get("access_token")
    user_response = httpx.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_response.json()
    return GoogleUser.model_validate(user_info)


@router.get("/microsoft")
async def auth_microsoft(code: str):
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    data = {
        "client_id": MICROSOFT_CLIENT_ID,
        "scope": "User.Read",
        "code": code,
        "redirect_uri": MICROSOFT_REDIRECT_URI,
        "grant_type": "authorization_code",
        "client_secret": MICROSOFT_CLIENT_SECRET,
    }
    headers = {"Accept": "application/json"}
    token_response = httpx.post(token_url, data=data, headers=headers)
    access_token = token_response.json().get("access_token")
    user_response = httpx.get(
        "https://graph.microsoft.com/v1.0/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_response.json()
    return MicrosoftUser.model_validate(user_info)
