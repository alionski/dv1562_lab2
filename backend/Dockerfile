FROM python:3.7

RUN mkdir /usr/src/lab_2
WORKDIR /usr/src/lab_2

RUN groupadd uwsgigroup && useradd -m -g uwsgigroup -s /bin/bash/ uwsgi

# first run $ pip freeze > requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3031

RUN chown -R uwsgi:uwsgigroup /usr/src/lab_2

USER uwsgi

CMD ["uwsgi", "--socket", ":3031", "--wsgi-file", "run.py", "--callable", "app", "--max-requests", "10", "--processes", "1", "--threads", "1", "--master" ]