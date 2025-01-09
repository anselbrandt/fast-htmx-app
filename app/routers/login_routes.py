from typing import Optional

from fastapi import APIRouter, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.constants import (
    ROOT_PATH,
    GITHUB_CLIENT_ID,
    GITHUB_REDIRECT_URI,
    GOOGLE_CLIENT_ID,
    GOOGLE_REDIRECT_URI,
    MICROSOFT_CLIENT_ID,
    MICROSOFT_REDIRECT_URI,
)

router = APIRouter(prefix="/login")

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def root(
    request: Request, response: Response, hx_request: Optional[str] = Header(None)
):
    context = {
        "request": request,
        "root_path": ROOT_PATH,
    }
    return templates.TemplateResponse("login.html", context)


@router.get("/github", response_class=HTMLResponse)
async def login_github(request: Request):
    link = f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope=repo%20user%3Aemail"
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "GitHub",
        "link": link,
    }
    return templates.TemplateResponse("oauth.html", context)


@router.get("/google", response_class=HTMLResponse)
async def login_google(request: Request):
    link = f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "Google",
        "link": link,
    }
    return templates.TemplateResponse("oauth.html", context)


@router.get("/microsoft", response_class=HTMLResponse)
async def login_microsoft(request: Request):
    link = f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id={MICROSOFT_CLIENT_ID}&response_type=code&redirect_uri={MICROSOFT_REDIRECT_URI}&response_mode=query&scope=https%3A%2F%2Fgraph.microsoft.com%2Fuser.read"
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "Microsoft",
        "link": link,
    }
    return templates.TemplateResponse("oauth.html", context)
