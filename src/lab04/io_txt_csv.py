from pathlib import Path
import csv 
from typing import Iterable, Sequence
import sys
sys.path.append(r'C:\Users\Alena\Documents\вуз\прога\python_labs')

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        return p.read_text(encoding=encoding)
    except UnicodeDecodeError :
        print( 'UnicodeDecodeError')
    except FileNotFoundError :
        print( 'FileNotFoundError')
#print(read_text(r'C:\Users\Alena\Documents\вуз\прога\python_labs\data\input.txt'))
print(read_text(r'C:\Users\Alena\Documents\вуз\прога\python_labs\data\test2.txt'))
'''
для смены кодировки , нужно при вызове read_text() после файла указать encoding = "НУЖНАЯ КОДИРОВКА"
'''
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    from src.lib.text import normalize, tokenize
    p = Path(path)
    rows = ' '.join(tokenize(normalize(rows)))
    print(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            if len(header) == 1:
                w.writerow(header)
        for r in rows:
            w.writerow(r)
write_csv(read_text(r'C:\Users\Alena\Documents\вуз\прога\python_labs\data\input.txt'),"data/check.csv")