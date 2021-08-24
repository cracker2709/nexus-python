FROM python:3.9-slim as build
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG=C.UTF-8
ENV PATH="/venv/bin:$PATH"
RUN mkdir -p /build
COPY . /build
WORKDIR /build
RUN apt update && apt install -y virtualenv && virtualenv /venv --python=python3 \
 && . /venv/bin/activate \
 && /venv/bin/python3 -m pip install --upgrade pip \
 && pip install -r requirements.txt \
 && pyb && WHL=$(find -type f -name "*nexus*.whl") \
 && pip install $WHL \
 && cp -r src/main/scripts/static src/main/scripts/templates src/main/scripts/certificate.pem docker-entrypoint.sh /venv/bin/

#
FROM python:3.9-slim as app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"
RUN apt update && apt install -y virtualenv
COPY --from=build /venv /venv
EXPOSE 5000
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

