class CardioTripod:
    @staticmethod
    def _validate_speed(speed:int) -> int:
        if not isinstance(speed, int):
            raise TypeError("Скорость должна быть числом")
        if  speed < 0 or speed > 50:
            raise ValueError("Будем более реалистичны")
        return speed
    @staticmethod
    def _validate_level(level:int) -> int:
        if not isinstance(level, int):
            raise TypeError("Уровень должен быть целым числом")
        if level < 0 or level > 5:
            raise ValueError("Уровень должен быть в границах от 1 до 5 (включительно)")
        return level


    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("Название обозначается строкой")
        if not isinstance(name, str):
            raise TypeError("Название обозначается строкой")
        return name.strip().lower()

    def __init__(self, name : str ,speed : int, level : int) -> None:
        self._name = self._validate_name(name)
        self._speed = self._validate_speed(speed)
        self._level = self._validate_level(level)


    @property
    def speed(self) -> int:
        return self._speed
    @property
    def level(self) -> int:
        return self._level
    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return (f'Тренажёр: {self.name}\n'
                f'Максимальная скорость: {self.speed} км/ч\n' 
                f'Уровень сложности : {self.level}'
               )
    def __repr__(self) -> str:
        return (f'CardioTripod(name = {self.name}, speed = {self.speed}, level = {self.level})')
    def __eq__(self,other):
        if not isinstance(other, CardioTripod):
            return False
        return self.name == other.name

class WeightTrainingEquipment: #мин вес ,(сравнение) макс вес , шаг изменения веса
    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("Название обозначается строкой")
        if not isinstance(name, str):
            raise TypeError("Название обозначается строкой")
        return name.strip().lower()
    @staticmethod
    def _validate_weight(weight: int) -> int:
        if not isinstance(weight, int):
            raise TypeError("Вес должен быть целым числом")
        if weight < 0 or weight > 250:
            raise ValueError("Будем более реалистичны")
        return weight
    @staticmethod
    def _validate_step(step: int) -> int:
        if not isinstance(step, int):
            raise TypeError("Шаг должен быть целым числом")
        if step < 1 or step > 10:
            raise ValueError("Будем более реалистичны")
        return step
    def __init__(self,name:str , weight_max : int,weight_min : int, step : int) -> None:
        self._name = self._validate_name(name)
        self._weight_max = self._validate_weight(weight_max)
        self._weight_min = self._validate_weight(weight_min)
        self._step = self._validate_step(step)
        if weight_min > weight_max:
            raise ValueError('Минимальный вес не может быть больше максимального')

    @property
    def weight_max(self) -> int:
        return self._weight_max
    @property
    def weight_min(self) -> int:
        return self._weight_min
    @property
    def step(self) -> int:
        return self._step
    @property
    def name(self) -> str:
        return self._name
    def __str__(self) -> str:
        return (f'Тренажёр: {self.name}\n'
                f'Максимальный вес: {self.weight_max} кг\n'
                f'Минимальный вес: {self.weight_min} кг\n'
                f'Шаг изменения веса : {self.step} кг\n'
                )
    def __repr__(self) -> str:
        return (f'WeightTrainingEquipment(name={self.name}, '
                f'weight_max={self.weight_max}, '
                f'weight_min={self.weight_min}, '
                f'step={self.step})')
    def __eq__(self,other):
        if not isinstance(other, WeightTrainingEquipment):
            return False
        return self.name == other.name







class Tripod:
    @staticmethod
    def _validate_type(type_obj: object):
        if not isinstance(type_obj, (WeightTrainingEquipment, CardioTripod)):
            raise TypeError(
                "Тренажёр должен быть объектом CardioTripod или WeightTrainingEquipment"
            )
        return type_obj

    @staticmethod
    def _validate_status(status: str) -> str:
        if not isinstance(status, str):
            raise TypeError("Статус должен быть строкой")
        status = status.strip().lower()
        if status not in ("занят", "свободен"):
            raise ValueError(
                f"Статус должен быть 'занят' или 'свободен', получено '{status}'"
            )
        return status

    @staticmethod
    def _validate_suitability(suitability: float) -> float:
        if not isinstance(suitability, (int, float)) or isinstance(suitability, bool):
            raise TypeError("Износ должен быть числом")
        suitability = float(suitability)
        if suitability < 0.0 or suitability > 1.0:
            raise ValueError("Износ должен быть от 0.0 до 1.0")
        return suitability

    @staticmethod
    def _validate_time(time: int) -> int:
        if not isinstance(time, int) or isinstance(time, bool):
            raise TypeError("Время должно быть целым числом")
        if time < 0:
            raise ValueError("Время не может быть отрицательным")
        return time

    @staticmethod
    def _validate_count(count: int) -> int:
        if not isinstance(count, int) or isinstance(count, bool):
            raise TypeError("Счётчик должен быть целым числом")
        if count < 0:
            raise ValueError("Счётчик не может быть отрицательным")
        return count


    MAX_SUITABILITY: float = 1.0

    def __init__(self,type_obj : object, status : str) -> None:
        self._type_obj = self._validate_type(type_obj)
        self._status = self._validate_status(status)
        self._suitability: float = 0.0
        self._count_people: int = 0
        self._time: int = 0

        if isinstance(type_obj, WeightTrainingEquipment):
            self._type = 'Силовой'
        else:
            if isinstance(type_obj, CardioTripod):
                self._type = 'Кардио'

    @property
    def type_obj(self):
        return self._type_obj

    @property
    def type(self) -> str:
        return self._type

    @property
    def status(self) -> str:
        return self._status

    @property
    def suitability(self) -> float:
        return self._suitability

    @property
    def count_people(self) -> int:
        return self._count_people

    @property
    def time(self) -> int:
        return self._time

    @time.setter
    def time(self, value: int) -> None:

        self._time = self._validate_time(value)


    def activate (self,minutes: int = 15) -> str:
        if self._status == "занят":
            raise RuntimeError("Тренажёр уже занят")
        if self._suitability >= self.MAX_SUITABILITY:
            raise RuntimeError(
                f"Износ {self._suitability * 100:.0f}% — нужен ремонт перед использованием"
            )

        minutes = self._validate_time(minutes)
        self._status = "занят"
        self._count_people += 1
        self._suitability = min(self.MAX_SUITABILITY, round(self._suitability + 0.15, 2))
        self._time += minutes

        if self._suitability >= 0.9:
            print(f"Внимание: износ {self._suitability * 100:.0f}% — скоро потребуется ремонт!")


    def off (self) :
        if self._status == "свободен":
            raise RuntimeError("Тренажёр уже свободен")
        self._status = "свободен"
    def fix (self) :
        if self._status == "занят":
            raise RuntimeError("Нельзя ремонтировать занятый тренажёр — сначала освободите")
        self._suitability = 0.0
        self._count_people = 0
        self._time = 0

    def add_session(self, minutes: int) -> None:
        if self._status != "занят":
            raise RuntimeError("Тренажёр свободен — сначала займите его (activate)")
        minutes = self._validate_time(minutes)
        if minutes == 0:
            raise ValueError("Длительность сессии должна быть > 0")
        self._time += minutes
        self._suitability = min(self.MAX_SUITABILITY, round(self._suitability + 0.05, 2))

    def needs_repair(self) -> bool:
        return self._suitability >= 0.9

    def __str__(self) -> str:
        wear_pct = self._suitability * 100
        return (
            f"[{self._type}] {self._type_obj.name} | "
            f"Статус: {self._status} | "
            f"Износ: {wear_pct:.0f}% | "
            f"Использований: {self._count_people} | "
            f"Время работы: {self._time} мин"
        )

    def __repr__(self) -> str:
        return (
            f"Tripod(type_obj={self._type_obj!r}, status={self._status!r}, "
            f"suitability={self._suitability}, count_people={self._count_people}, "
            f"time={self._time})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tripod):
            return NotImplemented
        return self._type_obj == other._type_obj











