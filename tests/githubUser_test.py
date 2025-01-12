from app.schemas import User, GithubUser, Provider


github_user_data = """
{
  "id": 1234567,
  "name": "user name",
  "email": "user@username.com"
}
"""


def test_github_user():
    githubUser = GithubUser.model_validate_json(github_user_data)
    assert isinstance(githubUser, GithubUser)


def test_github_base_user():
    githubUser = GithubUser.model_validate_json(github_user_data)
    user = User(
        id=githubUser.id,
        name=githubUser.name,
        email=githubUser.email,
        provider=Provider.GITHUB,
    )
    assert isinstance(user, User)
