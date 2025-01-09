from typing import Optional

from fastapi import APIRouter, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.constants import ROOT_PATH

router = APIRouter(prefix="/auth")

templates = Jinja2Templates(directory="templates")


@router.get("/login", response_class=HTMLResponse)
def root(
    request: Request, response: Response, hx_request: Optional[str] = Header(None)
):
    context = {
        "request": request,
        "root_path": ROOT_PATH,
    }
    return templates.TemplateResponse("login.html", context)
