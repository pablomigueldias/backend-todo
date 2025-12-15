from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class User(BaseModel):
    username: str
    password: str
    email: EmailStr


class UsersPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDB(User):
    id: int
