# python_labs 
## Лабораторная работа 1 
### Задание 1 
```
name = input('Имя:')
age = int(input('Возраст: '))
print(f'Привет {name}! Через год тебе будет  {age + 1 }') 
```
![image1!](./images/lab01/img1.png)
### Задание 2
```
num1 = float(input('a: ').replace(',','.'))
num2 = float(input('b: ').replace(',','.'))
sum = num1 + num2
avg = round (sum / 2 , 2) 
print('sum =' ,sum,'avg =', avg)
```
![image1!](./images/lab01/img2.png)
### Задание 3
```
price = float(input('Цена (₽): '))
discount = float(input('Скидка (%): '))
vat = float(input('НДС (%): '))
base = (price * (1 - discount/100))
vat_amount = (base * (vat/100) )
total = (base + vat_amount) 
print(f'База после скидки:{base:.2f}')
print(f'НДС:{vat_amount:.2f}')
print(f'Итого к оплате:{total:.2f}')
```
![image1!](./images/lab01/img3.png)
### Задание 4
```
minuts = int(input(''))
hours = minuts // 60 
min_ost = minuts % 60 
print(f'{hours}:{min_ost:02d}') 
```
![image1!](./images/lab01/img4.png)
### Задание 5
```
all_name = input('ФИО:')
all_name = ' '.join(all_name.split())
inic = ''
for el in all_name :
    if el.isupper():
        inic += el
print(f'Инициалы: {inic}')
print(f'Длинна (строки): {len(all_name)}')
```
![image1!](./images/lab01/img5.png)
### Задание 6 
```
kol_st = int(input())
och_uch = 0
zaoch_uch = 0
while kol_st != 0:
    uch = input()
    if 'True' in uch:
        och_uch += 1
    elif 'False' in uch:
        zaoch_uch += 1
    kol_st -= 1
print (och_uch,zaoch_uch)
```
![image1!](./images/lab01/img6.png)
### Задание 7
```
stroka = input()
stroka = stroka.split('.')[0]
itog_str = ''
frst_sim = 0
frst_num = 0
indx_first = 0
indx_secd = 0
for el in stroka :
    if el.isupper() and frst_sim == 0:
        frst_sim = 1
        itog_str += el 
        indx_first = stroka.index(el)
    if el.isdigit() and frst_num == 0 and frst_sim != 0:
        indx_secd = stroka.index(el) + 1
        itog_str += stroka[indx_secd]
        frst_num = 1
step = int(indx_secd) - int(indx_first)
for i in range(indx_secd + step,len(stroka),step ):
    itog_str += stroka[i]
print(itog_str)
```
![image1!](./images/lab01/img7.png)

## Лабораторная работа 2
### Задание 1 
#### min_max 
```
nums = [[3, -1, 5, 5, 0],[42],[-5, -2, -9],[],[1.5, 2, 2.0, -3.1]]
def min_max(nums):
    if list:
        return (min(nums),max(nums))
    else:
        return ('ValueError')
for i in nums:
    print(f"{i} -> {min_max(i)}")
```
![image1!](./images/lab02/arrays/min_max.png)
#### unique_sorted
```
nums = [[3, 1, 2, 1, 3],[],[-1, -1, 0, 2, 2],[1.0, 1, 2.5, 2.5, 0]]
def unique_sorted(nums):
    return sorted(list(set(nums)))
for i in nums:
    print(f'{i} -> {unique_sorted(i)}')
```
![image1!](./images/lab02/arrays/unique_sorted.png)
#### flatten
```
nums = [[[1, 2], [3, 4]],([1, 2], (3, 4, 5)),[[1], [], [2, 3]],[[1, 2], "ab"]]
def flatten(mat):
    st_itog = []
    for i  in list:
        if type(i) != str:
            for s in i :
                st_itog.append(s)
        else:
            return 'TypeError'
    return st_itog
for i in nums:
     print(f'{i} -> {flatten(i)}')
```
![image1!](./images/lab02/arrays/flatten.png)
### Задание 2
#### transpose
```
listik =[[[1, 2, 3]],[[1], [2], [3]] , [[1, 2], [3, 4]],[[1, 2], [3]]]
def transpose(mat: list[list[float | int]]) -> list[list] :
    pere_list = []
    for i in range(len(mat[0])) :
        if len(mat) == 1 or len(mat[0]) == len(mat[1]) :
            stroka = []
            for j in range(len(mat)) :
                stroka.append(mat[j][i])
            pere_list.append(stroka)
        else:
            return 'ValueError'
    return pere_list
for i in listik:
    print(f"{i} -> {transpose(i)}")
```
![image1!](./images/lab02/matrix/matrix.png)
#### row_sums
```
listik = [[[1, 2, 3], [4, 5, 6]],[[-1, 1], [10, -10]],[[0, 0], [0, 0]],[[1, 2], [3]]]
def row_sums(mat: list[list[float | int]]) -> list[float] :
    check = 1
    for i in range(1,len(mat)):
        if len(mat[i-1]) != len(mat[i]):
            check = 0
    if check:
        sums = [sum(x) for x in mat]
    else:
        return 'ValueError'
    return sums
for i in listik:
   print(f"{i} -> {row_sums(i)}")
```
![image1!](./images/lab02/matrix/row_sums.png)
#### col_sums
```
listik =[ [[1, 2, 3], [4, 5, 6]],[[-1, 1], [10, -10]],[[0, 0], [0, 0]],[[1, 2], [3]]] 
def col_sums(mat: list[list[float | int]]) -> list[float]:
    check = 1
    for i in range(1,len(mat)):
        if len(mat[i-1]) != len(mat[i]):
            check = 0
    if check:
        summ = [0 for i in range(len(mat[0]))]
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                summ[i] += mat[j][i]
        return summ 
    else:
        return 'ValueError'
for i in listik:
   print(f"{i} -> {col_sums(i)}")
```
![image1!](./images/lab02/matrix/col_sums.png)
### Задание 3
```
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

```
![image1!](./images/lab02/C.png)