from pathlib import Path
from src.lab04.io_txt_csv import read_text,  write_csv
from src.lib.text import normalize,tokenize,count_freq,top_n
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
data_dir = PROJECT_ROOT /"data" / "lab04"
input_name = input(str("Введи полное название входящего файла(по умолчанию input.txt) :"))
if not input_name:
    input_name = "input.txt"
output_name = input(str("Введи полное название сходящего файла(по умолчанию :report.csv) :"))
if not output_name:
    output_name = "report.csv"
coding = input(str("Введите кодировку если она не utf-8 (по умолчанию :utf-8):"))
#coding = ""
input_file = data_dir /input_name #
output_file = (data_dir /output_name)#
#print(data_dir)

try:
    if coding!= "":
        text = read_text(input_file,encoding=coding)
    else:
        text = read_text(input_file)
except FileNotFoundError:
    print(f"Файл '{input_file}' не найден!")

except UnicodeDecodeError:
    print(f"Невозможно прочитать с кодировкой {coding}")



if not text.strip():
    print("  Входной файл пустой")
    write_csv([], output_file, header=("word", "count"))
    print("\nВсего слов: 0")
    print("Уникальных слов: 0")


text = tokenize(normalize(text))

count_word = len(text)
text = count_freq(text)
count_uni_word = 0
for i in text.items():
    if i[1] == 1:
        count_uni_word += 1
text_for_report =[("word","count")]+top_n(text)
#print(text_for_report)
write_csv(text_for_report, data_dir/output_file)
print(f"Всего слов :      {count_word}")
print(f"Уникальных слов : {count_uni_word}")
for  (word, count) in text_for_report:
    print(f"{word:<12} {count:>5}")


