from typing import Optional

from fastapi import APIRouter, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.constants import (
    ROOT_PATH,
    GITHUB_LOGIN_LINK,
    GOOGLE_LOGIN_LINK,
    MICROSOFT_LOGIN_LINK,
)

router = APIRouter(prefix="/login")

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def login(
    request: Request, response: Response, hx_request: Optional[str] = Header(None)
):
    context = {
        "request": request,
        "root_path": ROOT_PATH,
    }
    return templates.TemplateResponse("login.html", context)


@router.get("/github", response_class=HTMLResponse)
async def login_github(request: Request):
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "GitHub",
        "link": GITHUB_LOGIN_LINK,
    }
    return templates.TemplateResponse("oauth.html", context)


@router.get("/google", response_class=HTMLResponse)
async def login_google(request: Request):

    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "Google",
        "link": GOOGLE_LOGIN_LINK,
    }
    return templates.TemplateResponse("oauth.html", context)


@router.get("/microsoft", response_class=HTMLResponse)
async def login_microsoft(request: Request):

    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "provider": "Microsoft",
        "link": MICROSOFT_LOGIN_LINK,
    }
    return templates.TemplateResponse("oauth.html", context)
