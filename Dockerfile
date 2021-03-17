FROM python:3.9.2-alpine3.13

RUN /sbin/apk add --no-cache libpq

COPY requirements.txt /pudding-api/requirements.txt
RUN /usr/local/bin/pip install --no-cache-dir --requirement /pudding-api/requirements.txt

ENV APP_VERSION="2021.2" \
    PYTHONUNBUFFERED="1" \
    TZ="Etc/UTC"

COPY get-data.py /pudding-api/get-data.py

ENTRYPOINT ["/usr/local/bin/python"]
