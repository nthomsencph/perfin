from sqlalchemy import Column, String

from db.config import Base


class User(Base):
    __tablename__ = "users"

    user_name = Column(String, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
