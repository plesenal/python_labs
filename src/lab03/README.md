## Лабораторная работа 3
### Задание A 
#### normalize
Реализовано с помощью проверок и использования нескольких методов 
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = ' '.join(text.split())
    for el in text:
        if el.isupper(): # проверка на верхний регистр 
            casefold = True 
            break
        else:
            casefold = False
    if casefold:
        text = text.casefold()
    if 'ё' not in text: # проверка на наличие Ё
        yo2e = False
    if yo2e:
        text = text.replace('ё','е')
    return text 
```
![image1!](images/lab03/A/img01.png)
#### tokenize
Реализовано с помощью регулярного выражения 
```python
def tokenize(text: str) -> list[str]:
    return re.findall(r'[а-я0-9-_]+',text) # поиск любых кобинаций из букв, цифр,'-','_' 
```
![image1!](python_labs//images/lab03/A/img02.png)
#### count_freq
Реализовано с помощью формирования словоря 
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    alf = list(sorted(set(tokens))) # отбираем различные слова и сортируем их
    chastots = {}
    for el in alf:
        chastots[el] = tokens.count(el) # к каждому ключу присваем значение , а именно сколько раз оно встречается в изначальном списке
    return chastots
```
#### top_n
Реализовано с помощью сортировке словоря и сокращения его длинны 
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    top_dict =dict(sorted(freq.items(), key=lambda item: (-item[1], item[0]))) # сортируем по убыванию значений , а потом по ключам  
    top = list(top_dict.items())[:n] # оставляем нужное количество для топа 
    return top
```
![image1!](python_labs//images/lab03/A/img03.png)

### Задание B
Скрипт `text_stats.py` читает одну строку текста из стандартного ввода (stdin), вызывает функцию из файла `lib/text.py` и выводит результат в стандартный вывод. 
```python
from lib.text import normalize as norm 
from lib.text import tokenize as t 
from lib.text import count_freq as c
from lib.text import top_n 
text = "Привет, мир! Привет!!!"
good_text = t(norm(text))
kol_slov = len(good_text)
kol_unik_slov = len(set(good_text)) 
top = top_n(c(good_text))
print(f'Всего слов: {kol_slov}')
print(f'Уникальных слов: {kol_unik_slov}')
print('Топ-5:')
for el in top:
    print(f'{el[0]} : {el[1]}')
```
![image1!](python_labs//images/lab03/imgB.png)
