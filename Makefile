.PHONY: convert install start stop

install:
    pip install -r requirements.txt

convert:
    python cli_convert.py tests/some.json output/some.csv

start:
    docker build -t json-to-csv .
    docker run -d -p 4000:80 --name python-container json-to-csv

stop:
    docker stop python-container
    docker rm python-container
