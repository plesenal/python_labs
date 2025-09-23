minuts = int(input(''))
hours = minuts // 60 
min_ost = minuts % 60 
days = 0
if hours > 24 :
    days = hours // 24
    hours = hours % 24
if days >= 1:
    print(f'{days} дн. {hours}:{min_ost:02d}') 
else:
    print(f'{hours}:{min_ost:02d}') 