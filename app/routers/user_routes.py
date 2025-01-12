from typing import Optional

from fastapi import APIRouter, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import jwt

from app.constants import ROOT_PATH, TOKEN_SECRET, TOKEN_ALGORITHM
from utils import generateFruitname

router = APIRouter(prefix="/user")

templates = Jinja2Templates(directory="templates")


@router.get("/profile", response_class=HTMLResponse)
def user_profile(
    request: Request, response: Response, hx_request: Optional[str] = Header(None)
):
    token = request.cookies.get("access_token")
    if token is None:
        context = {
            "request": request,
            "root_path": ROOT_PATH,
            "username": generateFruitname(),
        }
        return templates.TemplateResponse("profile.html", context)
    user = jwt.decode(token, TOKEN_SECRET, algorithms=[TOKEN_ALGORITHM])
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "username": user["name"],
    }
    return templates.TemplateResponse("profile.html", context)
