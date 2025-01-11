from typing import Optional
from urllib.parse import urlencode

from fastapi import APIRouter, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.constants import (
    ROOT_PATH,
    GITHUB_CLIENT_ID,
    GITHUB_OAUTH_URL,
    GITHUB_REDIRECT_URI,
    GOOGLE_CLIENT_ID,
    GOOGLE_OAUTH_URL,
    GOOGLE_REDIRECT_URI,
    MICROSOFT_CLIENT_ID,
    MICROSOFT_OAUTH_URL,
    MICROSOFT_REDIRECT_URI,
)

router = APIRouter(prefix="/login")

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def login(
    request: Request, response: Response, hx_request: Optional[str] = Header(None)
):
    context = {
        "request": request,
        "root_path": ROOT_PATH,
    }
    return templates.TemplateResponse("login.html", context)


@router.get("/github", response_class=HTMLResponse)
async def login_github(request: Request):
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "redirect_uri": GITHUB_REDIRECT_URI,
        "scope": "user:email",
    }
    link = f"{GITHUB_OAUTH_URL}?{urlencode(params)}"
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "GitHub",
        "link": link,
    }
    return templates.TemplateResponse("oauth.html", context)


@router.get("/google", response_class=HTMLResponse)
async def login_google(request: Request):
    params = {
        "response_type": "code",
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "scope": "openid profile email",
        "access_type": "offline",
    }
    link = f"{GOOGLE_OAUTH_URL}?{urlencode(params)}"
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "Google",
        "link": link,
    }
    return templates.TemplateResponse("oauth.html", context)


@router.get("/microsoft", response_class=HTMLResponse)
async def login_microsoft(request: Request):
    params = {
        "client_id": MICROSOFT_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": MICROSOFT_REDIRECT_URI,
        "response_mode": "query",
        "scope": "https://graph.microsoft.com/user.read",
    }
    link = f"{MICROSOFT_OAUTH_URL}?{urlencode(params)}"
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "Microsoft",
        "link": link,
    }
    return templates.TemplateResponse("oauth.html", context)
