from datetime import datetime, timedelta
import jwt

from app.constants import TOKEN_SECRET, TOKEN_ALGORITHM
from app.models import User


def create_jwt(user: User):
    expiration = datetime.now() + timedelta(hours=24)
    token = jwt.encode(
        {
            "name": user.name,
            "id": user.id,
            "email": user.email,
            "expiration": expiration.timestamp(),
        },
        TOKEN_SECRET,
        algorithm=TOKEN_ALGORITHM,
    )
    return token
