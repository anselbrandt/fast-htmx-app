from .auth_routes import router as auth_routes
from .login_routes import router as login_routes
from .user_routes import router as user_routes
from .files_routes import router as files_routes

__all__ = [auth_routes, login_routes, user_routes, files_routes]
