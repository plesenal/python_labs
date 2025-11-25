from .json_csv import *
from .csv_xlsx import csv_to_xlsx


def main() -> None:
    format_kon = input(
        "Выберите вариант конвертации файла (введите число): \n1. JSON -> CVS  \n2. CVS -> JSON\n3. CSV -> XLSX\n"
    )
    try:
        format_kon = int(format_kon)
    except ValueError:
        print("Введено не число :(")
        return

    if format_kon == 1:
        input_name = input(
            "Введи полное название входящего файла(по умолчанию people.json) :"
        )
        if not input_name:
            input_name = "people.json"
        output_name = input(
            "Введи полное название исходящего файла(по умолчанию :abc2.csv) :"
        )
        if not output_name:
            output_name = "abc2.csv"
        json_to_csv(input_name, output_name)
        print("Выполнено!")
    elif format_kon == 2:
        input_name = input(
            "Введи полное название входящего файла(по умолчанию cities.csv) :"
        )
        if not input_name:
            input_name = "cities.csv"
        output_name = input(
            "Введи полное название исходящего файла(по умолчанию :abc.json) :"
        )
        if not output_name:
            output_name = "abc.json"

        csv_to_json(input_name, output_name)
        print("Выполнено!")
    elif format_kon == 3:
        input_name = input(
            "Введи полное название входящего файла(по умолчанию cities.csv) :"
        )
        if not input_name:
            input_name = "cities.csv"
        output_name = input(
            "Введи полное название исходящего файла(по умолчанию :abc.xlsx) :"
        )
        if not output_name:
            output_name = "abc.xlsx"

        csv_to_xlsx(input_name, output_name)
        print("Выполнено!")
    else:
        print("Введено не правильное число :(")


if __name__ == "__main__":
    main()
