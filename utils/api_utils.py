import requests
from fastapi import HTTPException
from config import Config

def get_item_from_api(item_id: int):
    response = requests.get(f"http://{Config.API_HOST}:{Config.API_PORT}/items/{item_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Товар не найден.")
