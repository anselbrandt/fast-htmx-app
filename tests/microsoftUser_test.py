from app.user_models import User, MicrosoftUser, Provider

microsoft_user_data = """
{
  "id": "000462d53c8abac0",
  "displayName": "user name",
  "mail": "user.name@mail.com"
}
"""


def test_microsoft_user():
    microsoftUser = MicrosoftUser.model_validate_json(microsoft_user_data)
    assert isinstance(microsoftUser, MicrosoftUser)


def test_microsoft_base_user():
    microsoftUser = MicrosoftUser.model_validate_json(microsoft_user_data)
    user = User(
        provider_id=microsoftUser.id,
        name=microsoftUser.displayName,
        email=microsoftUser.mail,
        provider=Provider.MICROSOFT,
    )
    assert isinstance(user, User)
