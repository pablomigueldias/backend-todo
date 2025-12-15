from http import HTTPStatus

from fastapi import FastAPI

from backend_todo.schemas import Message

app = FastAPI(title='Todo Backend API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}
