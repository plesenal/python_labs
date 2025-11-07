from pathlib import Path
import csv 
from typing import Iterable, Sequence
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    parent = p.parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)
        
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        return p.read_text(encoding=encoding)
    except UnicodeDecodeError :
        print( 'UnicodeDecodeError')
    except FileNotFoundError :
        print( 'FileNotFoundError')
#print(read_text(r'прога\python_labs\data\input.txt'))
#print(read_text(r'прога\python_labs\data\test2.txt'))
'''
для смены кодировки , нужно при вызове read_text() после файла указать encoding = "НУЖНАЯ КОДИРОВКА"
'''
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    from lib.text import normalize, tokenize
    p = Path(path)
    #rows = (tokenize(normalize(rows)))
    #print([rows])
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            if len(header) == 1:
                w.writerow(header)
        for r in rows:
            print(r)
            w.writerow(r)
write_csv([("word","count"),("test",3)], "прога\\python_labs\\data\\check.csv") 
#write_csv(read_text(r'прога\python_labs\data\input.txt'),"прога\\python_labs\\data\\check.csv")