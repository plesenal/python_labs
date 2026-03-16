
class SportsmenInGym:
    def __init__(self, name: str,state : bool) -> None:
        self.name = name
        self.state = state
        self._membership_level : int = 0
        self._membership_state : bool = False
        self._number_of_visits : int = 0

    @property
    def membership_level(self) -> int:
        return self._membership_level
    @membership_level.setter
    def membership_level(self,value):
        self._membership_level = value
        if not isinstance(value, int):
            raise TypeError("Уровень абонимента должен быть целым числом ")
        if value > 3 or value < 1:
            raise ValueError("Уровень абонимента должен быть числом от 1 до 3")


    def __str__(self) -> str:
        sta_m = ''
        sta = ''
        if self.state:
            sta = 'Занимается'
        else:
            sta = 'Не в зале'
        if self.membership_state:
            sta_m = 'Действует'
        else:
            sta_m = ''
        return (f'Имя: {self.name}\n'
                f'Состояние: {sta}\n'
                f'Уровень абонимента: {self.membership_level}\n'
                f'Состояния абонимента : {self.membership_state}\n'
                f'Количество посещений за последний месяц : {self.number_of_visits}'
                )


def __repr__(self) -> str:
    return (f'SportsmenInGym(name={self.name}, '
            f'state = {self.state},'  
            f'membership_level = {self._membership_level},'
            f'membership_state = {self._membership_state },'
            f'number_of_visits ={self._number_of_visits},'
            )


def __eq__(self, other):
    return self.name == other.name and self.state == other.state