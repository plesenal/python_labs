from lab04.models import Trainer, EduSportsmen
def profitable(x):
    if x.price < 2000:
        return True
    return False

def make_type_filter(target_class):
    '''Фабрика для типов'''
    return lambda obj: isinstance(obj, target_class) 

def make_price_filter(max_price):
    '''фабрика для цен'''
    return lambda obj: obj.price <= max_price if hasattr(obj, 'price') else False


def make_name_sorter():
    '''фабрика для сортировки имен'''
    return lambda obj: obj.name

def make_price_sorter():
    '''фабрика для сортировки цен'''
    return lambda obj: obj.price if hasattr(obj, 'price') else 0

def make_state_type_sorter():
    '''фабрика для сортировки состояния (сначало те кто в зале) а потом по типу'''
    return lambda obj: (obj.state, 1 if  isinstance(obj, Trainer ) else 0)

class Activate:
    """
    Callable-объект, который переводит статус человека в 'В зале' .
    """
    def __call__(self, item):
        item.state = True
        return item
class Close:
    """
    Является callable-объектом. Переводит статус человека в 'Отсутствует' .
    """
    def __call__(self, item):
        item.state = False
        return item