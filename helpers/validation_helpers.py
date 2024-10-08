def validate_item_id(item_id: int) -> None:
    if item_id < 1:
        raise ValueError("ID должен быть положительным числом.")
