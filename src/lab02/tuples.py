input = [("Иванов Иван Иванович", "BIVT-25", 4.6),("Петров Пётр", "IKBO-12", 5.0),("Петров Пётр Петрович", "IKBO-12", 5.0),("  сидорова  анна   сергеевна ", "ABB-01", 3.999)]

def cut_name (fio:str):
    name = (' '.join(fio.split())).split(' ')
    scr_name = name[0] + ' '
    for i in range(1,len(name)):
        scr_name += name[i][0].upper() + '.'
    return scr_name

def format_record(rec: tuple[str, str, float]) -> str:
    if  (type(rec[0]) == str and type(rec[1]) == str and  type(rec[2]) == float  ) and (rec[0].strip() and rec[1].strip()):
        itog =f'{cut_name(rec[0])}, гр. {rec[1]}, {rec[2]:.2f}'
        return itog
    elif type(rec[0]) != str or type(rec[1]) != str or  type(rec[2]) != float: 
        return 'TypeError' 
    elif not rec[0].strip() or not rec[1].strip():
        return 'ValueError'
'''
TypeError - если не тот тип 
ValueError - если пустое ФИО или группа 
'''
for i in input:
   print(f"{i} -> {format_record(i)}")
