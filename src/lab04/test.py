from pathlib import Path
from src.lab04.io_txt_csv import read_text, write_csv


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
data_dir = PROJECT_ROOT / "data" / "lab04"
print(data_dir)

text = read_text(data_dir / "input.txt")  # возвращает строку
write_csv([("word", "count"), ("test", 3)], data_dir / "check.csv")  # создаст CSV
print(text)
