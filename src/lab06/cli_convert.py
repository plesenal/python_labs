import argparse

# Модуль src/lab06/cli_convert.py с подкомандами:
#
# json2csv --in data/samples/people.json --out data/out/people.csv
# csv2json --in data/samples/people.csv --out data/out/people.json
# csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
# (использовать функции из lab05)

import argparse
from src.lab05.json_csv import *
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument(
        "--in", dest="input", required=True, help="Полное название входящего файла"
    )
    p1.add_argument(
        "--out", dest="output", required=True, help="Полное название исходящего файла"
    )

    p2 = sub.add_parser("csv2json")
    p2.add_argument(
        "--in", dest="input", required=True, help="Полное название входящего файла"
    )
    p2.add_argument(
        "--out", dest="output", required=True, help="Полное название исходящего файла"
    )

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument(
        "--in", dest="input", required=True, help="Полное название входящего файла"
    )
    p3.add_argument(
        "--out", dest="output", required=True, help="Полное название исходящего файла"
    )

    args = parser.parse_args()

    if not args.cmd:
        parser.error("Не указана команда")

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)

    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)

    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
