from fastapi import FastAPI

from backend_todo.routers import auth, users

app = FastAPI(title='Todo Backend API')

app.include_router(users.router)
app.include_router(auth.router)
