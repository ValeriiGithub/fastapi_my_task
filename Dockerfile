FROM python:3.8-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--hosts", "0.0.0.0", "--port", "80"]

