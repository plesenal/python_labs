import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from io_txt_csv import read_text, write_csv
txt = read_text("data/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data1/check.csv")  # создаст CSV