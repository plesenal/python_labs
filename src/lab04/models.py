from lab01.validate import _validate_name,_validate_bool,_validate_level, _validate_visit
from lab04.interfaces import Video,Reg,Human
class SportsmenInGym(Human):
    gym_capacity: int = 12
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
        self.rep = Rep()
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
                f'{self.rep}\n'
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

from lab03.validate import validate_exp,validate_cnt,validate_age
class Trainer(SportsmenInGym,Reg,Video):
    def __init__(self,name: str,state : bool,age: int,experience : int, price: int,free_seats: int):
        super().__init__(name,state)
        self.age = age
        self.experience = experience
        self.price = price
        self.free_seats = free_seats
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        validate_age(value)
        self._age = value
    @property
    def experience(self) -> int:
        return self._experience
    @experience.setter
    def experience(self, value):
        validate_exp(value)
        if value > self._age - 18:
            raise ValueError('Укажите реальный опыт')
        self._experience = value
    def registration (self):
        self.free_seats -= 1
        return  self.free_seats
    def make_video(self):
        self.rep.respect()
    def add_seats (self,col):
        self.free_seats += col
        return self.free_seats

    def __str__(self):
        return( f"Тренер {self.name} {self._age} лет \nОпыт: {self._experience} лет \n Цена: {self.price} р/час тренировки \n Количество свободных мест: {self.free_seats} \n{self.rep}\n")


class EduSportsmen(SportsmenInGym,Reg,Video):
    def __init__(self,name:str,state:bool,_membership_level:int):
        super().__init__(name,state)
        self.cnt_wokot = 1 
        self.discount = _membership_level * 0.1
    @property
    def cnt_wokot(self):
        return self._cnt_wokot
    @cnt_wokot.setter 
    def cnt_wokot(self, value):
        validate_cnt(value)
        self._cnt_wokot = value
    def registration (self,cnt):
        self.cnt_wokot += cnt
    def complited_workout(self):
        if self.state:
            self.cnt_wokot -= 1
        else:
            raise ValueError('Нельзя завершить тренировку не находясь в зале')
    def make_video(self):
        self.rep.disrespect()
    def __str__(self):
        return(f'Спорстмен {self.name}\n{self.state}\nОсталось треникровок: {self.cnt_wokot} \nСкидка {self._membership_level * 10}%\n {self.rep}\n')
from lab01.validate import _validate_name
from lab02.validated import _validate_obj,_validate_add

class Gym:
    def __init__ (self, items: list[SportsmenInGym]):
        self.items = list(items)
        self.state = True 
        #super().__init__()
    def add(self,item):
        if _validate_obj(item) and _validate_add(self.items,item) and item.is_he_humane():
            self.items.append(item)
        elif not item.is_he_humane():
            raise 'Принимаем только человечных людей'
    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError('Обьект не найден')
    def remove_at(self,index):
        if -len(self.items)<= index < len(self.items):
            self.items.pop(index)
        else:
            raise ValueError('Обьект не найден')
    
    def sort_by_name (self):
        self.items.sort(key = lambda obj: obj.name)
    def get_all(self):
        return self.items.copy()
    
    def find_by_name(self,name:str):
        try:
            f_name = _validate_name(name)
            for item in self.items:
                if item.name == f_name :
                    return(item)
            return print('Имя не найдено')
        except:
            raise TypeError
    def open_gym (self):
        if self.state :
            raise ValueError('Зал уже открыт')
        else:
            self.state = True 
    def close_gym (self):
        if not self.state :
            raise ValueError('Зал уже закрыт')
        else:
            self.state = False
            for item in self.items:
                item.state = False
    def get_only_sportsmen(self):
        from lab03.models import EduSportsmen
        return [item for item in self.items if isinstance(item, EduSportsmen)]
    def get_only_trainer(self):
        from lab03.models import Trainer
        return [item for item in self.items if type(item) is Trainer]
    def get_only_video(self):
        return [item for item in self.items if isinstance(item, Video)]

    def __getitem__(self, index: int):
        return self.items[index]
    def __iter__(self) :
        return iter(self.items)
    def __str__(self):
        if not self.items:
            return "Тренажёрный зал пуст"
        status = 'Открыто' if self.state else "Закрыто"
        count = 0
        for it in self.items :
            if it.state :
                count += 1 
        athletes = "\n".join(f"  {i+1}. {obj}" for i, obj in enumerate(self.items))
        return f" {status} \n  Спортсмены в зале ({count}):\n{athletes}"
    def __len__(self) -> int:
        return len(self.items)

class Rep :
    def __init__(self) :
        self.rep : str = ''
    def respect(self):
        self.rep = '+ rep'
    def disrespect(self):
        self.rep = '- rep'
    def __str__(self):
        return f"{self.rep}"
        


