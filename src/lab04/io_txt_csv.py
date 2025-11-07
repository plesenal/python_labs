from pathlib import Path
import csv
from typing import Iterable, Sequence, Optional
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lib.text import tokenize, normalize


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        return p.read_text(encoding=encoding)
    except UnicodeDecodeError:
        print('UnicodeDecodeError')
        raise
    except FileNotFoundError:
        print('FileNotFoundError')
        raise


def write_csv(rows: list[tuple | list] | str,path: str | Path,header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    if isinstance(rows, (str, bytes)):
        rows_list = [(rows,)]
    else:
        rows_list = list(rows)

    expected_len: Optional[int] = None
    if header is not None:
            expected_len = len(header)
    if rows_list:
        if expected_len is None:
            expected_len = len(rows_list[0])
        for i, r in enumerate(rows_list):
            if len(r) != expected_len:
                raise ValueError(f"Строка {i} имеет длину {len(r)}, но ожидалось {expected_len}")
            
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(list(header))
        for r in rows_list:
            w.writerow(r)

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[2]

    in_path = repo_root / "data1" / "input.txt"
    out_path = repo_root / "data1" / "check.csv"

    print("cwd:", Path.cwd())
    print("Попытка прочитать:", in_path)

    try:
        text = read_text(in_path, encoding="utf-8")
    except FileNotFoundError:
        print(f"Файл не найден: {in_path}")
        raise
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки: {e}")
        raise
    write_csv(text, out_path)
    print("Записан:", out_path)
    read_text("data/input.txt")
