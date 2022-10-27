FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    netcat \
    wget \
    tesseract-ocr \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/tam.traineddata \
   https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata \
   https://github.com/tesseract-ocr/tessdata/raw/main/hin.traineddata \
   && mv -t /usr/share/tesseract-ocr/4.00/tessdata/ tam.traineddata \
   eng.traineddata hin.traineddata

WORKDIR /server

COPY Pipfile Pipfile.lock entry-point.sh  ./
RUN pipenv install --system

COPY . .

CMD /server/entry-point.sh & sleep infinity