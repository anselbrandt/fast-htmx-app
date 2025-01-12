from app.schemas import User, GoogleUser

google_user_data = """
{
  "id": "123456789012345678901",
  "email": "user.name@mail.com",
  "name": "user name"
}
"""


def test_google_user():
    googleUser = GoogleUser.model_validate_json(google_user_data)
    assert isinstance(googleUser, GoogleUser)
