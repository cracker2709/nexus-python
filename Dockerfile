FROM python:3 as intermediate
RUN mkdir -p /build
# those don't change often
ADD requirements.txt /build/requirements.txt
RUN python3 -m venv /venv \
     && . /venv/bin/activate \
     && /venv/bin/python3 -m pip install --upgrade pip \
     && pip install -r /build/requirements.txt

FROM python:3
# the data comes from the above container
COPY --from=intermediate /venv /venv
ADD requirements.txt /build/requirements.txt
# this command, starts from an almost-finished state every time
WORKDIR /build
RUN  /venv/bin/pip install -r requirements.txt
ADD docker-entrypoint.sh /build/docker-entrypoint.sh
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

