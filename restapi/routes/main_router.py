from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse,RedirectResponse

router = APIRouter()

# Эндпоинт для проверки состояния сервера
@router.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy"})

# Основной маршрут API
@router.get("/")
async def read_root():
    return RedirectResponse(url="/api/")

# Обработчик всех неопределённых маршрутов
@router.get("/api/{full_path:path}")
@router.get("/api/*")
async def catch_all(full_path: str = None):
    raise HTTPException(status_code=404)