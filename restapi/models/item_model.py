# restapi/models/item_model.py
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str = None
