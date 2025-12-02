import json
import pathlib
from models import Student
def students_to_json(students, path):
    path=pathlib.Path(path)
    data = [s.to_dict() for s in students]
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


def students_from_json(path):
    path=pathlib.Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден")
    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    students = [Student.from_dict(s) for s in data]
    return students
def main():
    students = [
        Student("Иванов И.И.", "2000/01/15", "ИВТ-101", 4.5),

        Student("Smith J.W.", "1999/11/20", "ENG-22", 3.8),

        Student("Сидорова А.А.", "2001/05/05", "МАТ-10", 5.0),

        Student("Петров П.П.", "2002/09/01", "ФИЗ-33", 0.0),
    ]
    #students_to_json(students, "./data/lab08/students_output.json")
    a = students_from_json("./data/lab08/students_input.json")
    for s in a:
        print(s)
if __name__ == "__main__":
    main()