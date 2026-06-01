# app.py
from lab06.container import TypedCollection
from lab04.models import Trainer, EduSportsmen
from lab07.models import ItemNotFoundError, DuplicateItemError, InvalidDataError
from lab07.storage import load_from_json, has_saved_data, save_to_json
from typing import List, Any

# Объявление внутренней коллекции слоя бизнес-логики
_gym_collection: TypedCollection[Any]

def init_app(load_data: bool) -> None:
    """Инициализирует внутреннюю коллекцию приложения.

    Args:
        load_data (bool): Флаг, определяющий, нужно ли загружать сохраненные данные.
    """
    global _gym_collection
    if load_data:
        _gym_collection = TypedCollection(items=load_from_json())
    else:
        _gym_collection = TypedCollection(items=[])

def check_saved_file_exists() -> bool:
    """Проверяет наличие ранее сохраненного файла с данными тренажерного зала.

    Returns:
        bool: True, если файл существует, иначе False.
    """
    return has_saved_data()

def shutdown_app() -> None:
    """Обеспечивает автоматическое сохранение текущей коллекции перед выходом."""
    save_to_json(_gym_collection.items)

def get_all_items() -> List[Any]:
    """Возвращает список всех объектов в коллекции тренажерного зала.

    Returns:
        List[Any]: Список тренеров и спортсменов.
    """
    return _gym_collection.items

def get_gym_status() -> bool:
    """Возвращает текущий рабочий статус тренажерного зала.

    Returns:
        bool: True, если зал открыт, иначе False.
    """
    return _gym_collection.state

def add_trainer(name: str, age: int, experience: int, price: int, free_seats: int) -> None:
    """Добавляет нового тренера с валидацией данных и проверкой на дубликаты имени.

    Raises:
        DuplicateItemError: Если тренер с таким именем уже зарегистрирован.
        InvalidDataError: Если данные не прошли валидацию внутренней модели Trainer.
    """
    duplicate = _gym_collection.find(lambda item: item.name.lower() == name.lower())
    if duplicate:
        raise DuplicateItemError(f"Ошибка: Тренер с именем '{name}' уже есть в базе.")
    
    try:
        new_trainer = Trainer(name=name, state=False, age=age, experience=experience, price=price, free_seats=free_seats)
        _gym_collection.add(new_trainer)
    except ValueError as e:
        raise InvalidDataError(f"Не удалось создать тренера. Причина: {e}")

def add_sportsman(name: str, membership_level: int) -> None:
    """Добавляет нового спортсмена с валидацией и проверкой на уникальность имени.

    Raises:
        DuplicateItemError: Если спортсмен с таким именем уже есть в системе.
        InvalidDataError: Если данные нарушают правила валидации модели EduSportsmen.
    """
    duplicate = _gym_collection.find(lambda item: item.name.lower() == name.lower())
    if duplicate:
        raise DuplicateItemError(f"Ошибка: Спортсмен с именем '{name}' уже есть в базе.")
    
    try:
        new_sportsman = EduSportsmen(name=name, state=False, _membership_level=membership_level)
        _gym_collection.add(new_sportsman)
    except ValueError as e:
        raise InvalidDataError(f"Не удалось создать спортсмена. Причина: {e}")

def get_item_name_by_index(display_index: int) -> str:
    """Возвращает имя объекта по его порядковому номеру для верификации удаления.

    Args:
        display_index (int): Порядковый номер строки из интерфейса таблицы (начиная с 1).

    Returns:
        str: Строковое имя найденного человека.

    Raises:
        ItemNotFoundError: Если указанный порядковый номер отсутствует в списке.
    """
    internal_index = display_index - 1
    if internal_index < 0 or internal_index >= len(_gym_collection.items):
        raise ItemNotFoundError(f"Элемент под номером {display_index} не существует в списке.")
    return str(_gym_collection.items[internal_index].name)

def remove_item_by_number(display_index: int) -> None:
    """Удаляет объект из коллекции по его порядковому номеру (начиная с 1).

    Args:
        display_index (int): Порядковый номер строки.

    Raises:
        ItemNotFoundError: Если индекс выходит за допустимые границы списка.
    """
    internal_index = display_index - 1
    if internal_index < 0 or internal_index >= len(_gym_collection.items):
        raise ItemNotFoundError(f"Элемент под номером {display_index} не существует в списке.")
    
    _gym_collection.remove_at(internal_index)

def sort_collection(strategy: int) -> None:
    """Выполняет сортировку коллекции в соответствии с выбранной стратегией.

    Args:
        strategy (int): 1 - Сортировка по имени, 2 - по цене, 3 - восстановление порядка.
    """
    if strategy == 1:
        _gym_collection.items.sort(key=lambda x: x.name.lower())
    elif strategy == 2:
        _gym_collection.items.sort(key=lambda x: getattr(x, 'price', 0))
    elif strategy == 3:
        _gym_collection.items = load_from_json()

def find_person_by_name(name: str) -> Any:
    """Осуществляет поиск человека в системе по его имени.

    Raises:
        ItemNotFoundError: Если человек с указанным именем не найден.
    """
    result = _gym_collection.find(lambda item: item.name.lower() == name.lower())
    if not result:
        raise ItemNotFoundError(f"Персона с именем '{name}' не найдена в системе зала.")
    return result

def filter_trainers_by_price(min_p: int, max_p: int) -> List[Any]:
    """Фильтрует список тренеров по диапазону стоимости их услуг."""
    trainers = _gym_collection.get_only_trainer()
    return [t for t in trainers if min_p <= t.price <= max_p]

def filter_people_by_state(in_gym: bool) -> List[Any]:
    """Фильтрует людей по критерию их фактического присутствия в зале."""
    return _gym_collection.filter(lambda item: item.state == in_gym)