FROM python:3.12-slim

EXPOSE 8080
WORKDIR /app/backend

RUN apt update \
    && apt install -y default-mysql-client \
    && apt-get -y install gcc libmariadb-dev pkg-config \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

COPY ./requirements.txt .
RUN pip install -U pip && pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app/* ./

CMD ["/bin/bash", "-c", "./app/run.sh"]