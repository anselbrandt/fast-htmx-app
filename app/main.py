from contextlib import asynccontextmanager
from subprocess import Popen, PIPE
from typing import Optional

from fastapi import FastAPI, Header, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.constants import ENV_MODE, ROOT_PATH
from app.routers import auth_routes, login_routes, user_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    if ENV_MODE == "DEV":
        process = Popen(
            ["./tailwindcss", "-o", "static/tailwind.css"], stdout=PIPE, stderr=PIPE
        )
        yield
        process.terminate()
    else:
        yield


app = FastAPI(root_path=ROOT_PATH, lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth_routes)
app.include_router(login_routes)
app.include_router(user_routes)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(
    request: Request, response: Response, hx_request: Optional[str] = Header(None)
):
    context = {
        "request": request,
        "root_path": ROOT_PATH,
    }
    return templates.TemplateResponse("index.html", context)
