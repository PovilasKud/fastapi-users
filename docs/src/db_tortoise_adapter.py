from fastapi_users.db import TortoiseUserDatabase

from .models import UserDB, UserModel

DATABASE_URL = "sqlite://./test.db"


def get_user_db():
    yield TortoiseUserDatabase(UserDB, UserModel)
