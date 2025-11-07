
def json_to_csv(json_path: str, csv_path: str) -> None:
    import json
    import csv
    from pathlib import Path
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    data_dir = PROJECT_ROOT / "data" / "lab05"
    path = Path(data_dir / json_path)
    with path.open(encoding="utf-8" ) as f:
        a = json.load(f)

    with open(data_dir/csv_path, "w", newline="", encoding="utf-8") as f:
        fieldnames = list(a[0].keys())
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(a)

    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
def csv_to_json(csv_path: str, json_path: str) -> None:
    pass
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
