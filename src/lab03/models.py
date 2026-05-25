from lab03.base import SportsmenInGym
from lab03.validate import validate_exp,validate_cnt,validate_age
class Trainer(SportsmenInGym):
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

    def add_seats (self,col):
        self.free_seats += col
        return self.free_seats

    def __str__(self):
        return( f"Тренер {self.name} {self._age} лет \nОпыт: {self._experience} лет \n Цена: {self.price} р/час тренировки \n Количество свободных мест: {self.free_seats} \n")


class EduSportsmen(SportsmenInGym):
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
        self.cnt_wokot -= 1
    def __str__(self):
        return(f'Спорстмен {self.name}\n{self.state}\nОсталось треникровок: {self.cnt_wokot} \nСкидка {self._membership_level * 10}%\n')
