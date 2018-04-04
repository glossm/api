FROM python:3.6.3-alpine3.6

RUN mkdir /code/
WORKDIR /code/
ADD ./ /code/

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
            gcc \
            make \
            libc-dev \
            musl-dev \
            linux-headers \
            pcre-dev \
            mariadb-dev \
            jpeg-dev \
            zlib-dev \
    && python -m venv /venv \
    && /venv/bin/pip install -U pip setuptools \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r requirements.txt" \
    && runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    && apk del .build-deps


# uWSGI will listen on this port
EXPOSE 8000

VOLUME ["/code"]

# Start uWSGI
CMD ["/venv/bin/uwsgi", "--ini", "uwsgi.ini"]
