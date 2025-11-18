import json
import csv
from pathlib import Path

path = "data/lab05/"

def json_to_csv(json_path: str, csv_path: str) -> None:

    json_file  = Path(path + 'samples/' + json_path)
    csv_file = Path(path + 'out/' + csv_path)

    if not json_file.exists() :
         raise FileNotFoundError(f"Файл не найден")

    try:
        with open(json_file,encoding="utf-8" ) as f:
            a = json.load(f)
    except json.JSONDecodeError :
        raise ValueError(f"Пустой JSON или неподдерживаемая структура")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = list(a[0].keys()) # порядок в ридми
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(a)

def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(path + 'samples/' + csv_path)
    json_file =  Path(path + 'out/' + json_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден")
    try:
        with csv_file.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception :
        raise ValueError(f"Ошибка чтения CSV")

    if not rows:
        raise ValueError("CSV файл пустой или не содержит заголовка")

    try:
        with json_file.open("w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")

