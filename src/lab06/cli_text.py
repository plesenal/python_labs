import argparse
from src.lib.text import  *
from src.lab04.io_txt_csv import *
# Модуль src/lab06/cli_text.py с подкомандами:
#
# stats --input <txt> [--top 5] — анализ частот слов в тексте (использовать функции из lab03);
# cat --input <path> [-n] — вывод содержимого файла построчно (с нумерацией при -n).
import sys, pathlib

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True,help="Путь к нужному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True,help="Путь к нужному файлу")
    stats_parser.add_argument("--top", type=int, default=5,help="Количество позиций в топе")

    args = parser.parse_args()

    if not args.command:
        parser.error("Не указана команда")

    if args.command == "cat":
        if args.n:
            try:
                text = read_text(args.input)
                for i, line in enumerate(text.splitlines(), 1):
                    print(f"{i} {line}")
            except FileNotFoundError:
                print("Файл не найден")
        else:
            try:
                text = read_text(args.input, args.n)
            except FileNotFoundError:
                print("Файл не найден")

    elif args.command == "stats":
        try:
            text = read_text(args.input)
            top = all_for_top_n(text,args.top)
            for word,col in top:
                print(f"{col} {word}")
        except FileNotFoundError:
            print("Файл не найден")

if __name__ == "__main__":
    main()
