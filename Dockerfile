FROM python:3.9-slim as build
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG=C.UTF-8
ENV PATH="/venv/bin:$PATH"
RUN mkdir -p /build
COPY requirements.txt /build/
WORKDIR /build
RUN python3 -m venv /venv \
    && . /venv/bin/activate \
    && /venv/bin/python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt

FROM python:3.9-slim as app
COPY . /build
WORKDIR /build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"
COPY --from=build /venv /venv
EXPOSE 5000
RUN . /venv/bin/activate && pyb && WHL=$(find -type f -name "*nexus*.whl") \
    && pip install $WHL \
    && cp -r src/main/scripts/static src/main/scripts/templates src/main/scripts/certificate.pem /venv/bin
CMD [ "python3", "src/main/scripts/nexus.py" ]

