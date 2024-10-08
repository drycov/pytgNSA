from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

from restapi.models.port_model import Port

router = APIRouter()

# Пример списка портов (вместо базы данных)
ports = []

# Маршрут для получения порта по ID
@router.get("/port/{port_id}", response_model=Port)
async def get_port(port_id: int):
    port = next((p for p in ports if p.id == port_id), None)
    if not port:
        raise HTTPException(status_code=404, detail="Port not found.")
    return port


# Маршрут для добавления нового порта
@router.post("/ports/", response_model=Port)
async def add_port(port: Port):
    # Проверка на дубликат
    if any(p.id == port.id for p in ports):
        raise HTTPException(status_code=400, detail="Port with this ID already exists.")
    ports.append(port)
    return port


# Маршрут для включения порта
@router.put("/port/{port_id}/enable", response_model=Port)
async def enable_port(port_id: int):
    port = next((p for p in ports if p.id == port_id), None)
    if not port:
        raise HTTPException(status_code=404, detail="Port not found.")

    port.status = "enabled"
    return port


# Маршрут для отключения порта
@router.put("/port/{port_id}/disable", response_model=Port)
async def disable_port(port_id: int):
    port = next((p for p in ports if p.id == port_id), None)
    if not port:
        raise HTTPException(status_code=404, detail="Port not found.")

    port.status = "disabled"
    return port


# Маршрут для изменения описания порта
@router.put("/port/{port_id}/description", response_model=Port)
async def update_port_description(port_id: int, description: str):
    port = next((p for p in ports if p.id == port_id), None)
    if not port:
        raise HTTPException(status_code=404, detail="Port not found.")

    port.description = description
    return port


# Маршрут для измерения длины кабеля
@router.put("/port/{port_id}/cable-length", response_model=Port)
async def update_cable_length(port_id: int, cable_length: float):
    port = next((p for p in ports if p.id == port_id), None)
    if not port:
        raise HTTPException(status_code=404, detail="Port not found.")

    port.cable_length = cable_length
    return port


# Маршрут для удаления порта
@router.delete("/port/{port_id}", status_code=204)
async def delete_port(port_id: int):
    for port in ports:
        if port.id == port_id:
            ports.remove(port)
            return
    raise HTTPException(status_code=404, detail="Port not found.")
