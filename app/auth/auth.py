import httpx

from app.constants import (
    GITHUB_CLIENT_ID,
    GITHUB_CLIENT_SECRET,
    GITHUB_REDIRECT_URI,
    GITHUB_TOKEN_URL,
    GITHUB_USER_URL,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    GOOGLE_REDIRECT_URI,
    GOOGLE_TOKEN_URL,
    GOOGLE_USER_URL,
    GITHUB_USER_EMAIL_URL,
    MICROSOFT_CLIENT_ID,
    MICROSOFT_CLIENT_SECRET,
    MICROSOFT_REDIRECT_URI,
    MICROSOFT_TOKEN_URL,
    MICROSOFT_USER_URL,
)
from app.models import GithubUser, GoogleUser, MicrosoftUser, Provider, User


def getGithubUser(code: str):
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
        "redirect_uri": GITHUB_REDIRECT_URI,
    }
    headers = {"Accept": "application/json"}
    token_response = httpx.post(GITHUB_TOKEN_URL, params=params, headers=headers)
    access_token = token_response.json().get("access_token")
    user_response = httpx.get(
        GITHUB_USER_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_response.json()
    if user_info["email"] is None:
        email_response = httpx.get(
            GITHUB_USER_EMAIL_URL,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        emails = email_response.json()
        merged = {**user_info, "email": emails[0]["email"]}
        githubUser = GithubUser.model_validate((merged))
        user = User(
            provider_id=githubUser.id,
            name=githubUser.name,
            email=githubUser.email,
            provider=Provider.GITHUB,
        )
        return user
    else:
        githubUser = GithubUser.model_validate_json(user_info)
        user = User(
            provider_id=githubUser.id,
            name=githubUser.name,
            email=githubUser.email,
            provider=Provider.GITHUB,
        )
        return user


def getGoogleUser(code: str):
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_response = httpx.post(GOOGLE_TOKEN_URL, data=data)
    access_token = token_response.json().get("access_token")
    user_response = httpx.get(
        GOOGLE_USER_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_response.json()
    googleUser = GoogleUser.model_validate(user_info)
    user = User(
        provider_id=googleUser.id,
        name=googleUser.name,
        email=googleUser.email,
        provider=Provider.GOOGLE,
    )
    return user


def getMicrosoftUser(code: str):
    data = {
        "client_id": MICROSOFT_CLIENT_ID,
        "scope": "User.Read",
        "code": code,
        "redirect_uri": MICROSOFT_REDIRECT_URI,
        "grant_type": "authorization_code",
        "client_secret": MICROSOFT_CLIENT_SECRET,
    }
    headers = {"Accept": "application/json"}
    token_response = httpx.post(MICROSOFT_TOKEN_URL, data=data, headers=headers)
    access_token = token_response.json().get("access_token")
    user_response = httpx.get(
        MICROSOFT_USER_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_response.json()
    microsoftUser = MicrosoftUser.model_validate(user_info)
    user = User(
        provider_id=microsoftUser.id,
        name=microsoftUser.displayName,
        email=microsoftUser.mail,
        provider=Provider.MICROSOFT,
    )
    return user
