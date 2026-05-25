def validate_exp(exp):
    try:
        a = int(exp)
    except:
        raise TypeError ('Не верный тип данных опыта')
    return True
def validate_age(age):
    if not isinstance(age,int):
        raise TypeError ('Не верный тип данных возраста')
    if age < 18 :
        raise ValueError('До совершеннолетия работай в другом месте')
    return True
def validate_cnt(cnt):
    if not isinstance(cnt,int):
        raise TypeError ('Не верный тип данных ')
    if cnt < 0 :
        raise ValueError ('Количество не может быть меньше 0')
    return True