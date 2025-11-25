import csv
from pathlib import Path
from openpyxl import Workbook

path = "data/lab05/"


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(path + "samples/" + csv_path)
    xlsx_file = Path(path + "out/" + xlsx_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден")
    if not csv_file.suffix.lower() == ".csv":
        raise ValueError(f"Неверный тип файла.")
    try:
        with csv_file.open(encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception:
        raise ValueError(f"Ошибка чтения CSV")
    if not rows:
        raise ValueError("CSV файл пуст")

    wb = Workbook()
    ws = wb.active
    ws.title = "Лист"

    for row in rows:
        ws.append(row)

    for stolb in ws.columns:
        max_length = 0
        stolb_letter = stolb[0].column_letter

        for cell in stolb:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        width_a = max(max_length, 8)
        ws.column_dimensions[stolb_letter].width = width_a
    wb.save(xlsx_file)

    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
