import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence],path: str | Path,header: tuple[str, ...] | None = None,encoding: str = "utf-8") -> None:
    p = Path(path)
    rows_list = list(rows)
    if rows_list:
        expected_length = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != expected_length:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, "
                    f"ожидалась длина {expected_length}"
                )

    if header and rows_list:
        if len(header) != len(rows_list[0]):
            raise ValueError(
                f"Длина заголовка ({len(header)}) не совпадает "
                f"с длиной строк данных ({len(rows_list[0])})"
            )

    
    with p.open("w", newline="", encoding=encoding) as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for row in rows_list:
            writer.writerow(row)


def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    parent = p.parent

    if str(parent) and str(parent) != ".":
        parent.mkdir(parents=True, exist_ok=True)
