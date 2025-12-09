from dataclasses import dataclass
from datetime import datetime,date
import re

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            b = datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")

        if not self.birthdate:
            raise ValueError("warning: birthdate is empty")
        today = date.today()
        if today.year < b.year :
            raise ValueError("warning: birthdate year is less than today's year")
        elif today.year == b.year and  today.month < b.month :
            raise ValueError("warning: birthdate month is less than today's month")
        elif today.year == b.year and today.month == b.month and today.day < b.day :
            raise ValueError("warning: birthdate day is less than today's day")

        if not isinstance(self.gpa, float):
            raise ValueError("warning: gpa is invalid")
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

        if not self.fio.strip():
            raise ValueError("warning: fio is empty")
        elif not re.match(r"^(?:['\"]?[А-ЯЁа-яёA-Za-z-]+ (?:(?:[А-ЯЁа-яёA-Za-z]\.){2}|[А-ЯЁа-яёA-Za-z]+))$", self.fio.strip()):
            raise ValueError("warning: fio is invalid")

        if not self.group.strip():
            raise ValueError("warning: group is empty")

    def age(self) -> int:
        b = datetime.strptime(self.birthdate, "%Y/%m/%d")
        today = date.today()
        if today.month < b.month or (today.month == b.month and today.day < b.day):
            return today.year - b.year - 1
        return today.year - b.year

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        if not isinstance(d, dict):
            raise TypeError("Data must be a dictionary")
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"])
        )



    def __str__(self):
        return f"Student ({self.fio}, {self.birthdate}, {self.group}, {self.gpa})"

def main():
    #s = Student("Иванов И.И.", "2000/01/20", "А-101", 4.5)
    #s = Student("Иванов И.И.", "20.01.2000", "А-101", 4.5)
    #s = Student("Иванов И.И.", "2000/01/20", "А-101", 8.0)
    #s = Student("Иванов И.И.", "2000/01/20", "", 4.0 )
    #d = {'fio': 'Иванов И.B.', 'birthdate': '2000/01/20', 'group': 'А-101', 'gpa': 4.0}
    #print(d)
    s = "2000/01/20"
    print(s.age())
    #print(s.to_dict())
    #print(Student.from_dict(d))
if __name__ == "__main__":
    main()