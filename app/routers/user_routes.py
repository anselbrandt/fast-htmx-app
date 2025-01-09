from typing import Optional

from fastapi import APIRouter, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.constants import ROOT_PATH
from utils import generateFruitname

router = APIRouter(prefix="/user")

templates = Jinja2Templates(directory="templates")


@router.get("/profile", response_class=HTMLResponse)
def root(
    request: Request, response: Response, hx_request: Optional[str] = Header(None)
):
    context = {
        "request": request,
        "root_path": ROOT_PATH,
        "username": generateFruitname(),
    }
    return templates.TemplateResponse("profile.html", context)
