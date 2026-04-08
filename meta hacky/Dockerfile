FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD bash -c "python inference.py; while true; do sleep 60; done"