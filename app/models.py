from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from sqlmodel import SQLModel, Field


class Provider(StrEnum):
    GITHUB = "GitHub"
    GOOGLE = "Google"
    MICROSOFT = "Microsoft"

    @classmethod
    def _missing_(cls, value: str):
        value = value.lower()
        for member in cls:
            if member.lower() == value:
                return member
        return None


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    email: EmailStr
    provider: str
    provider_id: str

    @field_validator("provider_id", mode="before")
    @classmethod
    def convert_id_to_string(cls, value):
        if isinstance(value, int):
            return str(value)
        return value


class GithubUser(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(extra="ignore")


class GoogleUser(BaseModel):
    id: str
    name: str
    email: EmailStr

    model_config = ConfigDict(extra="ignore")


class MicrosoftUser(BaseModel):
    id: str
    displayName: str
    mail: EmailStr

    model_config = ConfigDict(extra="ignore")
