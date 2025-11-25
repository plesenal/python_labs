import json
import csv
from pathlib import Path

path = "data/lab05/"


def json_to_csv(json_path: str, csv_path: str, test: bool = False) -> None:
    if test:
        json_file = Path(json_path)
        csv_file = Path(csv_path)
    else:
        json_file = Path(path + "samples/" + json_path)
        csv_file = Path(path + "out/" + csv_path)

    if not json_file.exists():
        raise FileNotFoundError(f"Файл не найден")

    try:
        with json_file.open(encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    first_keys = list(data[0].keys())
    if not first_keys:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str, test: bool = False) -> None:
    if test:
        json_file = Path(json_path)
        csv_file = Path(csv_path)
    else:
        csv_file = Path(path + "samples/" + csv_path)
        json_file = Path(path + "out/" + json_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден")
    try:
        with csv_file.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception:
        raise ValueError(f"Ошибка чтения CSV")

    if not rows:
        raise ValueError("CSV файл пустой или не содержит заголовка")

    try:
        with json_file.open("w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")
