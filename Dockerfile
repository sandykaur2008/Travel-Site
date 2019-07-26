FROM python:3.6-alpine

RUN adduser -D mytravels

WORKDIR /home/mytravels

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY mytravels.py config.py boot.sh .env ./
RUN chmod +x boot.sh

ENV FLASK_APP mytravels.py

RUN chown -R mytravels:mytravels ./
USER mytravels

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]