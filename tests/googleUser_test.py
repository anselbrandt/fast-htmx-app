from app.schemas import User, GoogleUser, Provider

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


def test_google_base_user():
    googleUser = GoogleUser.model_validate_json(google_user_data)
    user = User(
        id=googleUser.id,
        name=googleUser.name,
        email=googleUser.email,
        provider=Provider.GOOGLE,
    )
    assert isinstance(user, User)
