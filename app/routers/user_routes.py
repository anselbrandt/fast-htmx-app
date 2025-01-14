from typing import Optional

from fastapi import APIRouter, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.constants import ROOT_PATH
from app.auth import CurrentUser

router = APIRouter(prefix="/user")

templates = Jinja2Templates(directory="templates")


@router.get("/profile", response_class=HTMLResponse)
async def user_profile(
    user: CurrentUser,
    request: Request,
    response: Response,
    hx_request: Optional[str] = Header(None),
):
    if user is None:
        context = {
            "request": request,
            "root_path": ROOT_PATH,
        }
        return templates.TemplateResponse("login.html", context)
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "user": user,
    }
    return templates.TemplateResponse("profile.html", context)
