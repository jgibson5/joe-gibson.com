FROM python:3.6-alpine

RUN adduser -D admin

WORKDIR /home/joe-gibson

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY joe-gibson.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP joe-gibson.py

RUN chown -R admin:admin ./
USER admin

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]