.PHONY: convert install start stop

install:
    pip install -r requirements.txt

convert:
    python cli_convert.py tests/some.json output/some.csv

start:
    docker build -t fastapi_app .
    docker run -d -p 8000:8000 fastapi_app

stop:
    docker stop fastapi_app
