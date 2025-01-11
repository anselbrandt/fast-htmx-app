from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates

from app.auth import getGithubUser, getGoogleUser, getMicrosoftUser

router = APIRouter(prefix="/auth")

templates = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/github")
async def auth_github(code: str):
    user = getGithubUser(code)
    return user


@router.get("/google")
async def auth_google(code: str):
    user = getGoogleUser(code)
    return user


@router.get("/microsoft")
async def auth_microsoft(code: str):
    user = getMicrosoftUser(code)
    return user
