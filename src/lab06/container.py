from typing import TypeVar, Generic ,Union,Iterator, Protocol
from lab02.validated import _validate_add,_validate_obj
from lab04.models import SportsmenInGym
from lab04.interfaces import Video
from lab01.validate import _validate_name
from typing import Callable, Optional



class Activatable(Protocol):
    state: bool
class Priced(Protocol):
    price: int

T = TypeVar('T')
R = TypeVar('R')
P = TypeVar('P', bound=Priced)      
A = TypeVar('A', bound=Activatable)

class TypedCollection(Generic[T]):
    def __init__(self,items: list[T] = None) -> None:
        self.items: list[T] = list(items) if items is not None else []
        self.state = True 

    def add(self, item: T) -> None:
        if _validate_obj(item) and _validate_add(self.items,item) and item.is_he_humane():
            self.items.append(item)
        elif not item.is_he_humane():
            raise 'Принимаем только человечных людей'

    def remove(self, item: T) -> None:
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError('Обьект не найден')
    def remove_at(self,index) -> None:
        if -len(self.items)<= index < len(self.items):
            self.items.pop(index)
        else:
            raise ValueError('Обьект не найден')

    def get_all(self) -> list[T]:
        return list(self.items)
    
    def sort_by(self, key_func, reverse=False) -> 'TypedCollection':
        self.items.sort(key=key_func, reverse=reverse)
        return self


    def filter_by(self, predicate) -> 'TypedCollection':
        filtered_items = list(filter(predicate, self.items))
        return TypedCollection(filtered_items)
    
    def apply(self, func) -> 'TypedCollection':
        for item in self.items:
            func(item)
        return self
    
    def find_by_name(self,name:str) -> None:
        try:
            f_name = _validate_name(name)
            for item in self.items:
                if getattr(item, 'name', None) == f_name:
                    return item
            print('Имя не найдено')
            return None
        except Exception as e:
            raise TypeError from e
        
    def open_gym (self) -> None:
        if self.state :
            raise ValueError('Зал уже открыт')
        else:
            self.state = True 
    def close_gym (self) -> None:
        if not self.state :
            raise ValueError('Зал уже закрыт')
        else:
            self.state = False
            for item in self.items:
                item.state = False
    def get_only_sportsmen(self) -> list[T]:
        from lab03.models import EduSportsmen
        return [item for item in self.items if isinstance(item, EduSportsmen)]
    def get_only_trainer(self) -> list[T]:
        from lab03.models import Trainer
        return [item for item in self.items if type(item) is Trainer]
    def get_only_video(self) -> list[T]:
        return [item for item in self.items if isinstance(item, Video)]
   
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self.items:
            if predicate(item):
                return item
        return None
    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self.items if predicate(item)]
    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self.items]
    
    def __getitem__(self, index: int) -> Union[T, list[T]]:
        return self.items[index]
    def __iter__(self) -> Iterator[T]: 
        return iter(self.items)
    def __str__(self) -> str:
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