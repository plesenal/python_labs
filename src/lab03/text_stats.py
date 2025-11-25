from lib.text import normalize as norm
from lib.text import tokenize as t
from lib.text import count_freq as c
from lib.text import top_n

text = "Привет, мир! Привет!!!"
good_text = t(norm(text))
kol_slov = len(good_text)
kol_unik_slov = len(set(good_text))
top = top_n(c(good_text))
print(f"Всего слов: {kol_slov}")
print(f"Уникальных слов: {kol_unik_slov}")
print("Топ-5:")
for el in top:
    print(f"{el[0]} : {el[1]}")
