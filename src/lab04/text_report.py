from pathlib import Path
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
data_dir = PROJECT_ROOT / "data" / "lab04"
count_file = int(input("Введите количество входящих файлов (число):"))


def chek_text(input_file, coding):
    try:
        if coding != "":
            return tokenize(normalize(read_text(input_file, encoding=coding)))
        else:
            return tokenize(normalize(read_text(input_file)))
    except FileNotFoundError:
        return f"Файл '{input_file}' не найден!"

    except UnicodeDecodeError:
        return f"Невозможно прочитать с кодировкой {coding}"

    if not text.strip():
        return (
            ("  Входной файл пустой"),
            write_csv([], output_file, header=("word", "count")),
            ("\nВсего слов: 0\n", "Уникальных слов: 0"),
        )


def do_report(input_file, output_file, coding):
    text = chek_text(input_file, coding)
    count_word = len(text)
    text = count_freq(text)
    count_uni_word = 0
    for i in text.items():
        if i[1] == 1:
            count_uni_word += 1
    text_for_report = [("word", "count")] + top_n(text)
    # print(text_for_report)
    write_csv(text_for_report, data_dir / output_file)
    print(f"Всего слов :      {count_word}")
    print(f"Уникальных слов : {count_uni_word}")
    for word, count in text_for_report:
        print(f"{word:<12} {count:>5}")


def do_report_all(text, input_files):
    print(f"{'file'} {'word':<12} {'count':<5}")
    for i in range(0, len(text)):
        text_all = top_n(count_freq(text[i]))
        file = input_files[i]
        for word, count in text_all:
            print(f"{file} {word:<12} {count:<5}")


def main() -> None:
    all_text = []
    text_for_all = []
    codings = []
    input_files = []
    if count_file > 1:
        for i in range(count_file):
            input_name = input(
                "Введи полное название входящего файла(по умолчанию input.txt) :"
            )
            if not input_name:
                input_name = "input.txt"
            input_files.append(input_name)
            coding = input("Введите кодировку если она не utf-8 (по умолчанию :utf-8):")
            if not coding:
                coding = ""
            codings.append(coding)
            input_file = data_dir / input_name
            all_text += chek_text(input_file, coding)
            text_for_all.append(chek_text(input_file, coding))
        output_name = input(
            "Введи полное название сходящего файла(по умолчанию :report.csv) :"
        )
        if not output_name:
            output_name = "report.csv"
        all_text = " ".join(all_text)
        rezum_file = data_dir / "dadada.txt"
        with open(rezum_file, "w", encoding="utf-8") as file:
            file.write(all_text)
        print("=" * 50)
        do_report_all(text_for_all, input_files)
        print("~" * 50)
        do_report(rezum_file, output_name, coding="utf-8")

    elif count_file == 1:
        input_name = input(
            "Введи полное название входящего файла(по умолчанию input.txt) :"
        )
        if not input_name:
            input_name = "input.txt"
        output_name = input(
            "Введи полное название сходящего файла(по умолчанию :report.csv) :"
        )
        if not output_name:
            output_name = "report.csv"
        coding = input("Введите кодировку если она не utf-8 (по умолчанию :utf-8):")
        if not coding:
            coding = ""
        input_file = data_dir / input_name  #
        output_file = data_dir / output_name  #
        do_report(input_file, output_file, coding)


if __name__ == "__main__":
    main()
