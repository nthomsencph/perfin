from pydantic import BaseModel, Field


class User(BaseModel):
    name: str | None = Field(kw_only=False)
    auth_status: bool | None = Field(kw_only=False)
    username: str | None = Field(kw_only=False)

    def __bool__(self):
        return bool(self.auth_status)
