from pydantic import BaseModel

# Модель для устройства
class Device(BaseModel):
    id: int
    name: str
    type: str
    status: str