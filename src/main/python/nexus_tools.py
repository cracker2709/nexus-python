#!/usr/bin/env python3
import glob
import logging

import requests
from OpenSSL.crypto import load_certificate, FILETYPE_PEM

verbose = True

# init logging
log = logging.getLogger('NEXUS')
c_handler = logging.StreamHandler()
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
c_handler.setFormatter(log_format)
if verbose:
    print('Verbose mode enabled')
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.INFO)
log.addHandler(c_handler)

MAVEN_API_URL = "https://search.maven.org/"
MAVEN_QUERY_URL = "solrsearch/select?q="


def locate_cert_file():
    return glob.glob("**/*certificate.pem", recursive=True)[0]


def display_ca_bundle():
    file = locate_cert_file()
    with open(file, 'rb') as infile:
        custom_ca = infile.read()
        x509 = load_certificate(
            FILETYPE_PEM,
            custom_ca)
        log.debug(x509.get_subject())


def maven_search(group, artifact, version, extension):
    log.info("maven_search [IN]")
    c_url = "%s%s" % (MAVEN_API_URL, MAVEN_QUERY_URL)

    query_string = ""
    first = True

    if group != "":
        query_string += "g:\"%s\"" % group
        if first is False:
            query_string.replace("g:", " AND g:")
        first = False

    if artifact != "":
        query_string += "a:\"%s\"" % artifact
        if first is False:
            query_string.replace("a:", " AND a:")
        first = False

    if version != "":
        query_string += "v:\"%s\"" % version
        if first is False:
            query_string.replace("v:", " AND v:")
        first = False

    if extension != "":
        query_string += "p:\"%s\"" % version
        if first is False:
            query_string.replace("p:", " AND p:")

    c_url += query_string.replace(" ", "%20")
    log.info("Querying %s", c_url)
    value = requests.get(c_url, verify=locate_cert_file())
    log.info('Connection %s to OK.', c_url)
    return value.text
