# Конвертер JSON в CSV


## Установка

Для использования этого конвертера, клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

## Как использовать

1. Запустите скрипт `src/cli_convert.py`.
2. Укажите входной JSON файл и путь для сохранения CSV файла.

Пример использования:

```bash
python src/cli_convert.py some_json_.json output.csv
```

Это создаст файл `output.csv` с данными, сконвертированными из `some_json_.json`.
## Как использовать 2
1. Запустите скрипт `src/tests_many_json.py`.
2. Наполните папку tests файлами .json формата

```bash
python src/tests_many_json.py
```
Это создаст файлы в директории `output` в виде `filename.csv` с данными, сконвертированными из файлов директории `tests` 
## Тест для api
```cmd
curl -X POST -F "file=@C:/Users/someuser/..../file.json" http://localhost:8000/upload-file/

 uvicorn api:app --reload
```

## Примечание

Убедитесь, что у вас установлен Python 3.x и все зависимости из `requirements.txt` установлены:

```bash
pip install -r requirements.txt
```


