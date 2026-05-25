from lab04.interfaces import Human
def _validate_obj(obj):
    if not isinstance(obj, Human):
        raise TypeError('Не верный тип обьекта')
    else:
        return True
def _validate_add(sp,new):
    for item in sp:
        if item.name == new.name:
            raise ValueError ('Объект с таким именем уже существует')
    return True