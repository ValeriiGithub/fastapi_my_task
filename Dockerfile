FROM python:3.8-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8080"]

