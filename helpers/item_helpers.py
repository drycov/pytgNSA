from restapi.models import Item

def format_item(item: Item) -> dict:
    return {
        "id": item.id,
        "name": item.name,
        "description": item.description or "Нет описания",
    }
