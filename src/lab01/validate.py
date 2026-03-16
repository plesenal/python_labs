def _validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    if  len(name) > 20:
        raise ValueError('Имя слишком длинное , сократите')
    if len(name) < 2:
        raise ValueError('Имя должно состоять более чем из 1 символа')
    return name.strip().lower()
def _validate_bool(value):
    if not isinstance(value, bool):
        raise TypeError("Состояние должно быть логическим True / False")
    return value

def _validate_level(level):
    if not isinstance(level, int):
        raise TypeError("Уровень абонимента должен быть целым числом ")
    if level > 3 or level < 1:
        raise ValueError("Уровень абонимента должен быть числом от 1 до 3")
    return level
def _validate_visit(number):
    if not isinstance(number, int):
        raise TypeError("Количество посещений должно быть целым числом")
    if number < 0:
        raise ValueError("Количество посещений должно быть не отрицательным числом")
    return number