from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from .port_router import router as port_router

from restapi.models.device_model import Device

router = APIRouter()
# Пример списка устройств (вместо базы данных)
devices = []

# Маршрут для получения устройства по IP или ID
@router.get("/api/device/{identifier}", response_model=Device)
async def get_device(identifier: str):
    # Проверяем, является ли идентификатор IP или ID
    if identifier.isdigit():
        # Если идентификатор - это число, ищем по ID
        device = next((d for d in devices if d.id == int(identifier)), None)
    else:
        # Если это не число, ищем по IP
        device = next((d for d in devices if d.ip == identifier), None)

    if not device:
        raise HTTPException(status_code=404, detail="Device not found.")
    return device

# Маршрут для получения списка всех устройств
@router.get("/api/devices/", response_model=List[Device])
async def get_devices():
    return devices

# Маршрут для добавления нового устройства
@router.post("/api/devices/", response_model=Device)
async def add_device(device: Device):
    # Проверка на дубликат
    if any(d.id == device.id for d in devices):
        raise HTTPException(status_code=400, detail="Device with this ID already exists.")
    devices.append(device)
    return device

# Маршрут для удаления устройства по ID
@router.delete("/api/device/{device_id}", status_code=204)
async def delete_device(device_id: int):
    for device in devices:
        if device.id == device_id:
            devices.remove(device)
            return
    raise HTTPException(status_code=404, detail="Device not found.")

router.include_router(port_router,prefix="/device/{identifier}")
