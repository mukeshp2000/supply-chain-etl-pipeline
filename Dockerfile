FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements-etl.txt .

RUN pip install --no-cache-dir -r requirements-etl.txt

COPY src/ ./src/

RUN mkdir -p data/raw data/processed data/rejected logs

CMD ["python", "src/pipeline.py"]