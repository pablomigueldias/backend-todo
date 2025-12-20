from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    password: str
    email: EmailStr


class UsersPublic(BaseModel):
    username: str
    email: EmailStr
    id: int
    model_config = ConfigDict(from_attributes=True)


class Userlist(BaseModel):
    users: list[UsersPublic]


class Token(BaseModel):
    access_token: str
    token_type: str
