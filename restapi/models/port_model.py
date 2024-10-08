# Модель для порта
from typing import Optional
from pydantic import BaseModel


class Port(BaseModel):
    id: int
    device_id: int
    status: str  # Статус порта (например, "enabled", "disabled")
    description: str
    cable_length: Optional[float]  # Длина кабеля в метрах
