from src.lab05.json_csv import *
def main ()-> None:

    json_to_csv("people.json", 'abc.csv')

'''
data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
path = Path(data_dir/ "people1.json")
with path.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


data_dir = PROJECT_ROOT /"data"/"lab05"/ "people.json"
path = Path(data_dir/"lab05"/ "people.json")
with data_dir.open(encoding="utf-8") as f:
    a = json.load(f)
print(a)
'''
