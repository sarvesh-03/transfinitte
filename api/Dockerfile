FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    netcat \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /server

COPY Pipfile Pipfile.lock entry-point.sh  ./
RUN pipenv install --system

COPY . .

CMD /server/entry-point.sh & sleep infinity