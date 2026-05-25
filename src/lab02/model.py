from lab03.base import SportsmenInGym
from lab01.validate import _validate_name
from lab02.validated import _validate_obj,_validate_add

class Gym:
    def __init__ (self, items: list[SportsmenInGym]):
        self.items = list(items)
        self.state = True 
        #super().__init__()
    def add(self,item):
        if _validate_obj(item) and _validate_add(self.items,item):
            self.items.append(item)
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
            
        

