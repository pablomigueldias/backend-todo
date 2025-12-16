from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from backend_todo.schemas import User, UserDB, Userlist, UsersPublic

app = FastAPI(title='Todo Backend API')

database = []


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


@app.get('/users', status_code=HTTPStatus.OK, response_model=Userlist)
def list_users():
    return {'users': database}


@app.put(
    '/users/{user_id}', response_model=UsersPublic, status_code=HTTPStatus.OK
)
def update_user(user_id: int, user: User):

    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            detail='Não encontrado', status_code=HTTPStatus.NOT_FOUND
        )

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', status_code=HTTPStatus.OK)
def delete_user(user_id: int):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            detail='Não encontrado', status_code=HTTPStatus.NOT_FOUND
        )

    return database.pop(user_id - 1)
