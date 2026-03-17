from model import *


def scen1():
    print("======== 1. Создание обьектов и их сравнение============\n")
    sportsmen = [SportsmenInGym('Alex', False), SportsmenInGym('Alex', True), SportsmenInGym('Anna', True),
                 SportsmenInGym('Alex', False)]
    print('~~~~~~~~Объекты (спортсмены)~~~~~~~')
    for obj in sportsmen:
        print(obj)
    print('~~~~Сравнение спортсменов (по имени и состоянию)~~~~~\n')
    for obj2 in range(1, len(sportsmen)):
        print(repr(sportsmen[0]), repr(sportsmen[obj2]))
        print(sportsmen[0] == sportsmen[obj2])
        print('-' * 30)


def scen2():
    print("======== 2. Некорректный тип ============\n")
    try:
        obj1 = SportsmenInGym('Alex', 1)
    except TypeError as e:
        print(f"TypeError : {e}")
    try:
        obj1 = SportsmenInGym(['wadnadw'], True)
    except TypeError as e:
        print(f"TypeError : {e}")


def scen3():
    print("======== 3. Длинна имени выходит за диапазон ============\n")
    try:
        obj1 = SportsmenInGym('Alex' * 100, True)
    except ValueError as e:
        print(f"ValueError : {e}")
    try:
        obj1 = SportsmenInGym('', True)
    except ValueError as e:
        print(f"ValueError : {e}")
def scen4():
    print("======== 4. Демонстрация логических методов и использовние атрибута ============\n")
    print('-------- Атрибуты класса -----------\n'
          f"Вместимость зала: {SportsmenInGym.gym_capacity} (SportsmenInGym.gym_capacity)\n"
          f"Сейчас в зале: {SportsmenInGym._current_occupancy} (SportsmenInGym._current_occupancy)\n"
          )  # f"Пороги уровней: {SportsmenInGym.level_threshold}\n"
    alex = SportsmenInGym('Alex', False)
    anna = SportsmenInGym('Anna', False)
    print(alex)

    alex.enter()

    try:
        alex.exit()
    except ValueError as e:
        print(f"Ошибка выхода : {e}")
    alex.membership_activate()
    alex.enter()
    print(f'alex._current_occupancy : {alex._current_occupancy}')
    print(alex)
    alex.enter()

    print(f"Вместимость зала: {SportsmenInGym.gym_capacity} (SportsmenInGym.gym_capacity)\n"
          f"Сейчас в зале: {SportsmenInGym._current_occupancy} (SportsmenInGym._current_occupancy)\n")
    print('Anna')
    anna.membership_activate()
    anna.enter()
def scen5():
    print("======== 5. Демонстрация изменения через setter с использовнием атрибута ============\n")
    print(f'Пороги уровней: {SportsmenInGym.level_threshold}')
    alex = SportsmenInGym('Alex', True)
    print(alex)
    alex.membership_activate()
    for _ in range(150):
        alex.exit()
        alex.enter()
    print(alex)
def main():
    #scen1()
    #scen2()
    #scen3()
    #scen4()
    scen5()

if __name__ == '__main__':
    main()