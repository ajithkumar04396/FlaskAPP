FROM python:3.8-slim-buster

WORKDIR /var/www/

ADD . /var/www/

RUN pip install -r requirements.txt

RUN pip install gunicorn

EXPOSE 4000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:4000", "wsgi:app"]

