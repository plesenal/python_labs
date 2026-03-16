from validate import _validate_name,_validate_bool,_validate_level, _validate_visit
class SportsmenInGym:
    gym_capacity: int = 1
    _current_occupancy: int = 0
    level_threshold = {
        1: (51, 100),
        2: (101, 700),
        3: (701, float('inf'))
    }
    def __init__(self, name: str,state : bool) -> None:
        self._membership_level : int = 0
        self._membership_state : bool = False
        self._number_of_visits : int = 0

        self.name = _validate_name(name)
        self.state = _validate_bool(state)


    @property
    def membership_level(self) -> int:
        return self._membership_level
    @membership_level.setter
    def membership_level(self,value):
        self._membership_level = _validate_level(value)

    @property
    def membership_state(self) -> bool:
        return self._membership_state
    @membership_state.setter
    def membership_state(self,value: bool) -> None:
        self._membership_state = _validate_bool(value)

    @property
    def number_of_visits(self) -> int:
        return self._number_of_visits
    @number_of_visits.setter
    def number_of_visits(self,value: int) -> None:
        self._number_of_visits = _validate_visit(value)
        for level, (min_v, max_v) in SportsmenInGym.level_threshold.items():
            if min_v <= value <= max_v:
                self._membership_level = level
                break

    def change_name(self,name: str) -> None:
        self.name = _validate_name(name)

    def enter (self):
        try:
            if self.state:
                raise RuntimeError ('Вход уже был выполнен')
            if SportsmenInGym._current_occupancy >= SportsmenInGym.gym_capacity:
                raise OverflowError('Зал переполнен')
            if not self.membership_state:
                raise ValueError('Абонемент не действителен')
            else:
                self.state = True
                SportsmenInGym._current_occupancy += 1
                self.number_of_visits += 1
                print("Успешный вход\n")
        except (ValueError, OverflowError, RuntimeError) as e:
            print(f'Ошибка входа : {e}')

    def exit (self):
        if self.state :
            self.state = False
            SportsmenInGym._current_occupancy -= 1
            print("Успешный выход\n")
        else :
            raise ValueError('Необходимо сначала войти')

    def membership_activate(self):
        if self.membership_state:
            raise ValueError("Абонимент уже был активирован")
        else:
            self.membership_state = True
            print("Абонимент активирован")
    def membership_deactivate(self):
        if not self.membership_state:
            raise ValueError("Абонимент не активен ")
        elif self.state:
            raise ValueError('Необходимо выйти для деактивации абонимента')
        else:
            self.membership_state = False
            print("Абонимент деактивирован\n")




    def __str__(self) -> str:
        sta_m = ''
        sta = ''
        if self.state:
            sta = 'Зашел в зал'
        else:
            sta = 'Не в зале'
        if self.membership_state:
            sta_m = 'Действует'
        else:
            sta_m = 'Не действителен'
        return (f'Имя: {self.name}\n'
                f'Состояние: {sta}\n'
                f'Уровень абонимента: {self.membership_level}\n'
                f'Состояния абонимента : {sta_m}\n'
                f'Количество посещений  : {self.number_of_visits}\n'
                )

    def __repr__(self) -> str:
        return (f'SportsmenInGym(name={self.name},'
                f'state = {self.state},'  
                f'membership_level = {self._membership_level},'
                f'membership_state = {self._membership_state },'
                f'number_of_visits ={self._number_of_visits})\n' )


    def __eq__(self, other):
        try:
            if not isinstance(other, SportsmenInGym):
                return NotImplemented
            return self.name == other.name and self.state == other.state
        except AttributeError:
            return False
