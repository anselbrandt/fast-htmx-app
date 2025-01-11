from enum import StrEnum

from pydantic import BaseModel, EmailStr, field_validator


class Provider(StrEnum):
    GITHUB = "GitHub"
    GOOGLE = "Google"
    MICROSOFT = "Microsoft"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.lower() == value:
                return member
        return None


class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    provider: Provider

    @field_validator("id", mode="before")
    @classmethod
    def convert_id_to_string(cls, value):
        if isinstance(value, int):
            return str(value)
        return value


class GithubUser(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        extra = "ignore"


class GoogleUser(BaseModel):
    id: str
    name: str
    email: EmailStr

    class Config:
        extra = "ignore"


class MicrosoftUser(BaseModel):
    id: str
    displayName: str
    mail: EmailStr

    class Config:
        extra = "ignore"
