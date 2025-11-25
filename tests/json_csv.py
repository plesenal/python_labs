import pytest
import json
import csv
from lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst), True)

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_json_to_csv_ValueError1(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text(json.dumps([{}], ensure_ascii=False, indent=2), encoding="utf-8")

    with pytest.raises(ValueError) as excinfo:
        json_to_csv(str(src), str(dst), True)
    assert excinfo.type == ValueError


def test_json_to_csv_FileNotFoundError(tmp_path: Path):
    with pytest.raises(FileNotFoundError) as excinfo:
        json_to_csv("vsaghvs.json", "uaidh.csv", True)

    assert excinfo.type == FileNotFoundError


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = ["name,age,city", "Alice,22,SPB", "Bob,25,Moscow"]
    src.write_text("\n".join(data), encoding="utf-8")
    csv_to_json(str(src), str(dst), True)
    with dst.open(encoding="utf-8") as f:
        data2 = json.load(f)

    expected = [
        {"name": "Alice", "age": "22", "city": "SPB"},
        {"name": "Bob", "age": "25", "city": "Moscow"},
    ]
    assert data2 == expected


def test_csv_to_json_ValueError(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError) as excinfo:
        csv_to_json(str(src), str(dst), True)
    assert excinfo.type == ValueError


def test_csv_to_json_FileNotFoundError(tmp_path: Path):
    with pytest.raises(FileNotFoundError) as excinfo:
        csv_to_json("vsaghvs.csv", "uaidh.json", True)

    assert excinfo.type == FileNotFoundError
