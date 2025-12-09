import csv
from pathlib import Path
from typing import List, Dict, Any
from lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)

    def _read_all(self):
        rows: List[Dict[str, Any]] = []

        with self.path.open("r", encoding="utf-8",newline="") as f:
            reader = csv.DictReader(f)
            for raw in reader:
                norm_row: Dict[str, Any] = {}
                for k, v in raw.items():
                    # k может быть None если в CSV больше полей чем заголовков — пропускаем такие колонки
                    if not k:
                        continue
                    key = k.strip().lower()
                    norm_row[key] = v.strip() if (v is not None) else ""

                # привести gpa к float (если возможно), иначе None
                gpa_raw = norm_row.get("gpa", "")
                if gpa_raw != "":
                    try:
                        norm_row["gpa"] = float(gpa_raw.replace(",", "."))
                    except (ValueError, TypeError):
                        norm_row["gpa"] = None
                else:
                    norm_row["gpa"] = None

                rows.append(norm_row)

        return rows

    def _ensure_storage_exists(self) -> None:
        dirpath = self.path.parent or Path(".")
        dirpath.mkdir(parents=True, exist_ok=True)
        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def list(self):
        students: List[Student] = []
        rows = self._read_all()
        for r in rows:
            fio = r.get("fio")
            birthdate = r.get("birthdate")
            group = r.get("group")
            gpa = r.get("gpa")
            students.append(Student(fio,birthdate,group,gpa))
        return students

    def add(self, student: Student):
        need_header = not self.path.exists() or self.path.stat().st_size == 0
        with self.path.open("a", encoding="utf-8",newline="") as f:
            strok =[student.fio ,student.birthdate , student.group , student.gpa]
            csv.writer(f).writerow(strok)


    def find(self, substr: str):
        rows = self._read_all()
        resz = [r for r in rows if substr in r["fio"]]
        if len(resz) > 0:
            return resz
        else:
            return "Студент не найден"

    def remove(self, fio: str):
        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            new_rows = []
            for i, r in enumerate(rows):
                if r[0] != fio:
                    new_rows.append(r)

        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(new_rows)
        return True

    def update(self, fio: str, **fields):
        rows = self._read_all()
        for i in rows:
            if i["fio"] == fio:
                for k, v in fields.items():
                    i[k] = v
                break
        headers = ["fio", "birthdate", "group", "gpa"]
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for r in rows:
                out = {
                    "fio": r.get("fio"),
                    "birthdate": r.get("birthdate"),
                    "group": r.get("group"),
                    "gpa": (r.get("gpa") if r.get("gpa") is not None else "")
                }
                writer.writerow(out)
        return True
    def stats(self) -> dict:
        rows = self._read_all()
        gpa =[]
        groups = set()
        for r in rows:
            gpa.append(r.get("gpa"))
            groups.add(r.get("group"))
        group_count = dict()
        for r in rows:
            for g in groups:
                if r.get("group") == g:
                    group_count[g] = group_count.get(g, 0) + 1

        sorted_students = sorted(rows, key=lambda r: (-float(r['gpa']), r['fio']))
        stat ={
            "count": len(rows),
            "min_gpa": min(gpa),
            "max_gpa": max(gpa),
            "avg_gpa":(sum(gpa)/ len(gpa)) ,
            "groups": group_count,
            "top_5_students": sorted_students[:5],
        }
        return stat
def main():
    group = Group('./data/lab09/students.csv')
    g = []
    students = Student('Штефанов Алексей','2003/07/22','SE-01',3.9)
    group.add(students)
    #group.remove('Штефанов Алексей')
    #group.update('Штефанов Алексей',gpa = 4.6,group = 'FBK-25')
    #print(group.list())
    #print(group.find("Павлова Мария"))
    print(group.stats())
if __name__ == "__main__":
    main()