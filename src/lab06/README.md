## Лабораторная работа 5
1. Желательно чтоб было виртуальное окружение
``` 
pip install  .
```
если нет 
```
pip install -r requirements.txt
```
2. Команды запуска (из корня проекта)
``` 
python -m src.lab06.cli_text cat --input (полный путь к файлу)
python -m src.lab06.cli_text cat --input (полный путь к файлу) --n (для вывода с нумерацией)

python -m src.lab06.cli_text stats --input (полный путь к файлу)
python -m src.lab06.cli_text stats --input (полный путь к файлу) --top 3 (для указание количества позиций в топе)

python -m src.lab06.cli_convert json2csv --in (название входящего файла) --out (название исходящего файла)
python -m src.lab06.cli_convert csv2json --in (название входящего файла) --out (название исходящего файла)
python -m src.lab06.cli_convert csv2xlsx --in (название входящего файла) --out (название исходящего файла)
```
### Примеры работы
![image1!](./images/lab06/img1.png)
![image1!](./images/lab06/img2.png)
![image1!](./images/lab06/img3.png)
![image1!](./images/lab06/img4.png)
![image1!](./images/lab06/img5.png)