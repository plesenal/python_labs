# storage.py
import json
import os
from typing import List, Dict, Any
from lab04.models import Trainer, EduSportsmen

FILEPATH: str = "gym_data.json"

def has_saved_data(filepath: str = FILEPATH) -> bool:
    """Проверяет, существует ли файл сохранения на диске.

    Args:
        filepath (str): Путь к файлу.

    Returns:
        bool: True, если файл существует, иначе False.
    """
    return os.path.exists(filepath) and os.path.getsize(filepath) > 0


def save_to_json(items: List[Any], filepath: str = FILEPATH) -> None:
    """Сохраняет список объектов коллекции в JSON-файл.

    Args:
        items (List[Any]): Список объектов для сериализации.
        filepath (str): Путь к файлу сохранения.
    """
    serialized_data: List[Dict[str, Any]] = []
    
    for item in items:
        class_name: str = item.__class__.__name__
        data: Dict[str, Any] = {
            "__class__": class_name,
            "name": item.name,
            "state": item.state
        }
        
        if class_name == "Trainer":
            data.update({
                "age": item.age,
                "experience": item.experience,
                "price": item.price,
                "free_seats": item.free_seats
            })
        elif class_name == "EduSportsmen":
            data.update({
                "membership_level": item.membership_level
            })
            
        serialized_data.append(data)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(serialized_data, f, ensure_ascii=False, indent=4)


def load_from_json(filepath: str = FILEPATH) -> List[Any]:
    """Загружает данные из JSON-файла и восстанавливает объекты классов.

    Args:
        filepath (str): Путь к файлу для чтения.

    Returns:
        List[Any]: Список воссозданных объектов.
    """
    if not has_saved_data(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data: List[Dict[str, Any]] = json.load(f)
            
        items: List[Any] = []
        for obj_dict in data:
            cls_name: str = obj_dict.get("__class__", "")
            name: str = obj_dict.get("name", "Unknown")
            state: bool = obj_dict.get("state", False)
            
            if cls_name == "Trainer":
                trainer = Trainer(
                    name=name,
                    state=state,
                    age=obj_dict.get("age", 0),
                    experience=obj_dict.get("experience", 0),
                    price=obj_dict.get("price", 0),
                    free_seats=obj_dict.get("free_seats", 0)
                )
                items.append(trainer)
            elif cls_name == "EduSportsmen":
                sportsman = EduSportsmen(
                    name=name,
                    state=state,
                    _membership_level=obj_dict.get("membership_level", 1)
                )
                items.append(sportsman)
                
        return items
    except (json.JSONDecodeError, KeyError, ValueError):
        return []