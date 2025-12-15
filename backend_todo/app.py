from http import HTTPStatus

from fastapi import FastAPI

from backend_todo.schemas import Message, User, UserDB, UsersPublic

app = FastAPI(title='Todo Backend API')

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UsersPublic)
def create_user(user: User):
    user_with_id = UserDB(
        id=len(database) + 1,
        username=user.username,
        password=user.password,
        email=user.email,
    )
    database.append(user_with_id)
    return user_with_id
