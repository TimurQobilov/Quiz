from fastapi import APIRouter
from database.userservice import *
from database.testservice import *
# объект нашего компонента (аналог blueprint в Flask)
user_router = APIRouter(prefix="/user",
                        tags=["Пользовательская часть"])

@user_router.post("/register")
async def add_user(username:str, phone_number:str):
    result = add_user_db(name=username, phone_number=phone_number)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": "ошибка"}


