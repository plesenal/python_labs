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
