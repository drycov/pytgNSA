from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Зависимость для проверки прав администратора
async def get_current_admin(token: str = Depends(oauth2_scheme)):
    # Здесь должна быть ваша логика для проверки токена и прав администратора
    # Например, декодирование токена и проверка роли пользователя
    return True  # Предположим, что проверка прошла успешно

@router.get("/admin/")
async def read_admin_dashboard(current_admin: bool = Depends(get_current_admin)):
    return JSONResponse(status_code=200, content={"message": "Welcome to the admin dashboard!"})

@router.get("/admin/users/")
async def get_users(current_admin: bool = Depends(get_current_admin)):
    # Логика для получения списка пользователей
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return JSONResponse(status_code=200, content={"users": users})

@router.post("/admin/users/")
async def create_user(user: dict, current_admin: bool = Depends(get_current_admin)):
    # Логика для создания пользователя
    return JSONResponse(status_code=201, content={"message": "User created", "user": user})

@router.delete("/admin/users/{user_id}")
async def delete_user(user_id: int, current_admin: bool = Depends(get_current_admin)):
    # Логика для удаления пользователя
    return JSONResponse(status_code=204)
