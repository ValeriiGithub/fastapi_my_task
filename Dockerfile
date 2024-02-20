FROM pyton:3.8-slim
LABEL authors="Valerii"

ENTRYPOINT ["top", "-b"]

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--hosts", "0.0.0.0", "--port", "80"]

