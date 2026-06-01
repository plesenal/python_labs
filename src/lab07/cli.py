# cli.py
from typing import List, Any
from lab07.app import (
    check_saved_file_exists, get_all_items, add_sportsman, add_trainer,
    sort_collection, find_person_by_name, filter_trainers_by_price,
    filter_people_by_state, get_item_name_by_index, remove_item_by_number,
    get_gym_status
)

def ask_for_load_data() -> bool:
    """Запрашивает у пользователя подтверждение на загрузку существующих данных.

    Returns:
        bool: True, если данные нужно восстановить, False — если начать сессию с нуля.
    """
    if not check_saved_file_exists():
        print("\n[Информация]: Сохраненный файл данных не найден. Начинаем с чистой коллекции.")
        return False
        
    choice: str = input("Обнаружены сохраненные данные. Загрузить их из файла? (y/n): ").strip().lower()
    if choice == 'y':
        print("[Успех]: Сохраненные данные успешно восстановлены.")
        return True
    else:
        print("[Информация]: Старые данные проигнорированы. Инициализирован пустой зал.")
        return False

def print_menu() -> None:
    """Выводит в консоль главное интерактивное меню приложения."""
    print("\n" + "="*60)
    print("                 УПРАВЛЕНИЕ ТРЕНАЖЕРНЫМ ЗАЛОМ")
    print("="*60)
    print("1. Показать всех людей (Таблица)")
    print("2. Добавить тренера")
    print("3. Добавить спортсмена")
    print("4. Сортировать коллекцию")
    print("5. Найти человека по имени")
    print("6. Фильтр тренеров по цене")
    print("7. Фильтр людей по статусу в зале")
    print("8. Удалить человека из системы")
    print("0. Выход")
    print("="*60)

def safe_input_int(prompt: str) -> int:
    """Запрашивает числовой ввод у пользователя с циклической защитой от некорректных строк."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("[Внимание]: Требуется ввести целое число.")

def get_deletion_confirmation(item_name: str) -> bool:
    """Запрашивает текстовое подтверждение перед выполнением опасной операции.

    Args:
        item_name (str): Имя целевого объекта.
    """
    choice: str = input(f"Удалить \"{item_name}\"? (y/n): ").strip().lower()
    return choice == 'y'

def print_table(items: List[Any]) -> None:
    """Форматирует и выводит список переданных объектов в виде красивой таблицы."""
    if not items:
        print("\n[Информация]: Список пуст.")
        return
    print("\n" + "-"*90)
    print(f"{'№':<3} | {'Тип объекта':<14} | {'Имя':<15} | {'В зале?':<8} | {'Дополнительные параметры'}")
    print("-"*90)
    for idx, item in enumerate(items, 1):
        cls_name: str = item.__class__.__name__
        st: str = "Да" if item.state else "Нет"
        if cls_name == "Trainer":
            info: str = f"Возраст: {item.age} | Опыт: {item.experience}л | Цена: {item.price}р"
        else:
            info = f"Уровень: {item.membership_level} | Оставшиеся тренировки: {item.cnt_wokot}"
        print(f"{idx:<3} | {cls_name:<14} | {item.name:<15} | {st:<8} | {info}")
    print("-"*90)

def show_all_items_action() -> None:
    """Выводит информацию о работе тренажерного зала и текущую таблицу людей."""
    status: str = "ОТКРЫТ" if get_gym_status() else "ЗАКРЫТ"
    print(f"\nТекущий статус зала: {status}")
    print_table(get_all_items())

def add_trainer_action() -> None:
    """Вызывает интерактивную форму ввода характеристик нового тренера."""
    print("\n--- Форма добавления тренера ---")
    name: str = input("Имя: ").strip()
    age: int = safe_input_int("Возраст: ")
    exp: int = safe_input_int("Опыт (лет): ")
    price: int = safe_input_int("Цена за час: ")
    seats: int = safe_input_int("Свободные места: ")
    add_trainer(name, age, exp, price, seats)
    print("[Успех]: Тренер добавлен.")

def add_sportsman_action() -> None:
    """Вызывает интерактивную форму регистрации спортсмена."""
    print("\n--- Форма добавления спортсмена ---")
    name: str = input("Имя: ").strip()
    level: int = safe_input_int("Уровень абонемента (1-3): ")
    add_sportsman(name, level)
    print("[Успех]: Спортсмен добавлен.")

def sort_collection_action() -> None:
    """Отображает подменю стратегий сортировки и передает управление бизнес-логике."""
    print("\nСортировать по:")
    print("1. Имени (алфавиту)")
    print("2. Цене")
    print("3. Исходному порядку (дате добавления)")
    strategy: int = safe_input_int("Выберите стратегию сортировки: ")
    if strategy in [1, 2, 3]:
        sort_collection(strategy)
        print("[Успех]: Коллекция отсортирована.")
    else:
        print("[Ошибка]: Неверная стратегия сортировки.")

def find_by_name_action() -> None:
    """Спрашивает имя и отображает найденную запись."""
    name: str = input("\nВведите имя для поиска: ").strip()
    person: Any = find_person_by_name(name)
    print_table([person])

def filter_by_price_action() -> None:
    """Задает границы фильтрации и выводит отфильтрованных тренеров."""
    p_min: int = safe_input_int("Минимальная цена: ")
    p_max: int = safe_input_int("Максимальная цена: ")
    print_table(filter_trainers_by_price(p_min, p_max))

def filter_by_state_action() -> None:
    """Фильтрует людей по критерию присутствия."""
    print("1. В зале\n2. Вне зала")
    choice: int = safe_input_int("Выберите статус: ")
    print_table(filter_people_by_state(choice == 1))

def remove_item_action() -> None:
    """Безопасно удаляет объект с предварительным выводом его имени и подтверждением y/n."""
    num: int = safe_input_int("\nВведите порядковый номер объекта для удаления: ")
    item_name: str = get_item_name_by_index(num)
    
    if get_deletion_confirmation(item_name):
        remove_item_by_number(num)
        print(f"[Успех]: Объект \"{item_name}\" успешно удален.")
    else:
        print("[Отмена]: Операция удаления отменена пользователем.")