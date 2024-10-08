from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/users/")
async def get_users():
    # Логика для получения списка пользователей для обычных пользователей
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return JSONResponse(status_code=200, content={"users": users})
