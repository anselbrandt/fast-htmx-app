from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.auth import getGithubUser, getGoogleUser, getMicrosoftUser
from app.constants import COOKIE_NAME
from app.db import get_session, add_user
from app.auth import create_jwt

router = APIRouter(prefix="/auth")

templates = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(COOKIE_NAME)
    response.status_code = status.HTTP_200_OK
    return response


@router.get("/github")
async def auth_github(code: str, session: Session = Depends(get_session)):
    user = getGithubUser(code)
    new_user = add_user(session, user)
    jwt_token = create_jwt(new_user)
    response = JSONResponse(content={**user.model_dump()})
    response.set_cookie(
        key=COOKIE_NAME,
        value=jwt_token,
        httponly=True,
        max_age=86400,
        secure=True,
        samesite="strict",
    )
    return response


@router.get("/google")
async def auth_google(code: str, session: Session = Depends(get_session)):
    user = getGoogleUser(code)
    new_user = add_user(session, user)
    jwt_token = create_jwt(new_user)
    response = JSONResponse(content={**user.model_dump()})
    response.set_cookie(
        key=COOKIE_NAME,
        value=jwt_token,
        httponly=True,
        max_age=86400,
        secure=True,
        samesite="strict",
    )
    return response


@router.get("/microsoft")
async def auth_microsoft(code: str, session: Session = Depends(get_session)):
    user = getMicrosoftUser(code)
    new_user = add_user(session, user)
    jwt_token = create_jwt(new_user)
    response = JSONResponse(content={**user.model_dump()})
    response.set_cookie(
        key=COOKIE_NAME,
        value=jwt_token,
        httponly=True,
        max_age=86400,
        secure=True,
        samesite="strict",
    )
    return response
