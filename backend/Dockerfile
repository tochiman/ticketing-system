FROM python:3.12-slim

ENV ROOT_PATH=/api

EXPOSE 8080
WORKDIR /app/backend

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


COPY ./app/* ./

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port","8080"]
