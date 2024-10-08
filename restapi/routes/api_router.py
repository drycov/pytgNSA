from fastapi import APIRouter
from fastapi.responses import JSONResponse,RedirectResponse
from .main_router import router as main_router
from .admin_router import router as admin_router
from .users_router import router as users_router
from .device_router import router as device_router

router = APIRouter()

@router.get("/api/")
async def get_routes():
    routes = router.routes
    routes_info = []

    for route in routes:
        methods = list(route.methods)  # Преобразуем множество методов в список
        
        routes_info.append({
            'path': route.path,
            'methods': methods,
        })

    return JSONResponse(status_code=200, content={"status": 200, "api": "v1", "routes": routes_info})

router.include_router(main_router)
router.include_router(admin_router,prefix="/api")
router.include_router(users_router,prefix="/api")
router.include_router(device_router,prefix="/api")




