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

test2 =["привет мир", "hello,world!!!", "2025 год","по-настоящему круто",'emoji 😀 не слово']
def tokenize(text: str) -> list[str]:
    return re.findall(r'[а-яa-z0-9-_]+',text)

for el in test2:
    print(f'{repr(el)} -> {repr(tokenize(el))}')

test3 = [["a","b","a","c","b","a"],["bb","aa","bb","aa","cc"]]
def count_freq(tokens: list[str]) -> dict[str, int]:
    alf = list(sorted(set(tokens)))
    chastots = {}
    for el in alf:
        chastots[el] = tokens.count(el)
    return chastots

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    top_dict =dict(sorted(freq.items(), key=lambda item: (-item[1], item[0])))
    top = list(top_dict.items())[:n]
    return top

'''
# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
'''