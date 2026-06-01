# main.py
from lab07.cli import (
    sort_collection_action, ask_for_load_data, print_menu, show_all_items_action,
    add_sportsman_action, add_trainer_action, filter_by_price_action,
    filter_by_state_action, find_by_name_action, remove_item_action
)
from lab07.models import ItemNotFoundError, DuplicateItemError, InvalidDataError
from lab07.app import init_app, shutdown_app
import sys

def main() -> None:
    should_load: bool = ask_for_load_data()
    init_app(load_data=should_load)
    
    while True:
        print_menu()
        try:
            choice = int(input("Выберите пункт меню: "))
        except ValueError:
            print("\n[Ошибка ввода]: Требуется ввести номер пункта меню цифрой.")
            continue

        if choice == 0:
            shutdown_app()
            print("\nДанные сохранены. Выход из программы. До свидания!")
            sys.exit(0)

        try:
            if choice == 1:
                show_all_items_action()
            elif choice == 2:
                add_trainer_action()
            elif choice == 3:
                add_sportsman_action()
            elif choice == 4:
                sort_collection_action()
            elif choice == 5:
                find_by_name_action()
            elif choice == 6:
                filter_by_price_action()
            elif choice == 7:
                filter_by_state_action()
            elif choice == 8:
                remove_item_action()
            else:
                print(f"\n[Предупреждение]: Пункта {choice} нет в меню.")

        except ItemNotFoundError as error:
            print(f"\n❌ [ОШИБКА]: {error}")
        except DuplicateItemError as error:
            print(f"\n❌ [ОШИБКА БИЗНЕС-ЛОГИКИ]: {error}")
        except InvalidDataError as error:
            print(f"\n❌ [ОШИБКА ВАЛИДАЦИИ]: {error}")
        except Exception as error:
            print(f"\n⚠️ [КРИТИЧЕСКАЯ СИСТЕМНАЯ ОШИБКА]: {error}")

if __name__ == "__main__":
    main()