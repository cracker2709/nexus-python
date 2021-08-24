FROM python:3 as build
RUN mkdir -p /build
COPY . /build
WORKDIR /build
RUN python3 -m venv /venv \
 && . /venv/bin/activate \
 && /venv/bin/python3 -m pip install --upgrade pip \
 && pip install -r /build/requirements.txt \
 && pyb && WHL=$(find -type f -name "*nexus*.whl") \
 && pip install $WHL \
 && cp -r src/main/scripts/static src/main/scripts/templates src/main/scripts/certificate.pem docker-entrypoint.sh /venv/bin/

#
FROM python:3
ENV PATH="/venv/bin:$PATH"
# # the data comes from the above container
COPY --from=build /venv /venv
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

