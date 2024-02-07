FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENV HOST 0.0.0.0
ENV PORT 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
