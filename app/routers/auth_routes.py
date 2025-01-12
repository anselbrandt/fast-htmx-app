from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.auth import getGithubUser, getGoogleUser, getMicrosoftUser
from app.db import get_session, add_user
from app.models import User

router = APIRouter(prefix="/auth")

templates = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/github")
async def auth_github(code: str, session: Session = Depends(get_session)) -> User:
    user = getGithubUser(code)
    new_user = add_user(session, user)
    return new_user


@router.get("/google")
async def auth_google(code: str, session: Session = Depends(get_session)) -> User:
    user = getGoogleUser(code)
    new_user = add_user(session, user)
    return new_user


@router.get("/microsoft")
async def auth_microsoft(code: str, session: Session = Depends(get_session)) -> User:
    user = getMicrosoftUser(code)
    new_user = add_user(session, user)
    return new_user
