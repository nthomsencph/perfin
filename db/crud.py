from contextlib import contextmanager

from db.config import get_session
from db.models.users import User


class UserCRUD:
    @classmethod
    def retrieve_users(cls):
        with get_session() as session:
            _users = session.query(User).all()
            return [user.as_dict() for user in _users]

    @classmethod
    def retrive_users_for_auth(cls):
        users: list[dict] = cls.retrieve_users()
        return {
            "usernames": {
                d["user_name"]: {
                    key: value for key, value in d.items() if key != "user_name"
                }
                for d in users
            }
        }
