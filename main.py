import pydantic
from fastapi import FastAPI, Request
from api.users_api.users import user_router
app = FastAPI(docs_url="/")
# делаем миграции (первичной - первый раз только сработает)
from database import Base, engine
Base.metadata.create_all(bind=engine)
# регистрируем компонент( роутер)
app.include_router(user_router)

# запуск uvicorn main:app --reload
