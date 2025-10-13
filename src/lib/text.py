import re 
test1 = ["ПрИвЕт\nМИр\t","ёжик, Ёлка","Hello\r\nWorld","  двойные   пробелы  "]
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = ' '.join(text.split())
    for el in text:
        if el.isupper():
            casefold = True 
            break
        else:
            casefold = False
    if casefold:
        text = text.casefold()
    if 'ё' not in text:
        yo2e = False
    if yo2e:
        text = text.replace('ё','е')
    return text 
'''
for el in test:
    print(f"{repr(el)} -> {repr(normalize(el))}")
'''
test2 =["привет мир", "hello,world!!!", "2025 год","по-настоящему круто",'emoji 😀 не слово']
def tokenize(text: str) -> list[str]:
    return re.findall(r'[а-я0-9-_]+',text)
'''
for el in test2:
    print(f"{repr(el)} -> {repr(tokenize(el))}")
'''
test3 = [["a","b","a","c","b","a"],["bb","aa","bb","aa","cc"]]
def count_freq(tokens: list[str]) -> dict[str, int]:
    alf = list(sorted(set(tokens)))
    chastots = {}
    for el in alf:
        chastots[el] = tokens.count(el)
    return chastots
'''
for el in test3:
    print(f"{repr(el)} -> {repr(count_freq(el))}")
'''
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    top_dict =dict(sorted(freq.items(), key=lambda item: (item[1], item[0])))
    top = list(freq.items())[:n]
    return top
for el in test3:
    print(f"токены {repr(el)} -> частоты {repr(count_freq(el))} ;\nчастоты {count_freq(el)}, n=2 -> топ {top_n(count_freq(el),n = 2)}\n")