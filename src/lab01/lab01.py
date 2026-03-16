
сlass SportsmenInGym:
    def __init__(self, name: str,state : str,membership_level : str,membership_state: bool,number_of_visits: int,) -> None:
        self.name = name
        self.state = state
        self._membership_level = membership_level
        self._membership_state = membership_state
        self._number_of_visits = number_of_visits

    @property
    def membership_level(self) -> int:
        return self._membership_level
    @membership_level.setter
    def membership_level(self,value):
        self._membership_level = value
        if not isinstance(value, int):
            raise TypeError("Уровень должен быть целым числом ")
        if value > 3 or value < 1:
            raise ValueError("Уровень должен быть числом от 1 до 3")


    def __str__(self) -> str:
        return (f'Имя: {self.name}\n'
                f'Состояние: {self.weight_max} кг\n'
                f'Минимальный вес: {self.weight_min} кг\n'
                f'Шаг изменения веса : {self.step} кг\n'
                )


def __repr__(self) -> str:
    return (f'WeightTrainingEquipment(name={self.name}, '
            f'weight_max={self.weight_max}, '
            f'weight_min={self.weight_min}, '
            f'step={self.step})')


def __eq__(self, other):
    if not isinstance(other, WeightTrainingEquipment):
        return False
    return self.name == other.name