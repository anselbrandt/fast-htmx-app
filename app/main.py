from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, Header, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db import init_db
from app.constants import ROOT_PATH
from app.routers import auth_routes, login_routes, user_routes
from app.tailwind import tailwind


@asynccontextmanager
async def lifespan(app: FastAPI):
    process = None
    try:
        process = tailwind()
        init_db()
        yield
    finally:
        if process:
            process.terminate()


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


@app.get("/health")
async def health(request: Request, response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "healthy"}
