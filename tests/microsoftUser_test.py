from app.schemas import User, MicrosoftUser


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
