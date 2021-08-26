#!/usr/bin/env python3
import os
import logging
from werkzeug.utils import redirect

from NexusForm import NexusForm
from nexus_tools import maven_search, display_ca_bundle
from flask import Flask, render_template, request, url_for, jsonify, flash

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

app = Flask(__name__, template_folder='templates')

api = "/service/rest/v1/search/assets"

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=['get', 'post'])
@app.route("/index.html")
@app.route("/statics/img/html")
def index():
    form = NexusForm()
    kwargs = dict(
        logo="static/img/nexus-logo.png",
        wallpaper="static/img/wallpaper.jpg",
        form=form,
    )
    if form.validate_on_submit():
        log.info("Search data Value : %s", form.submit.data)
        log.info("Search New data Value : %s", form.submit_new.data)
        group = form.group.data
        artifact = form.artifact.data
        version = form.version.data
        extension = form.extension.data

        if form.submit.data:
            form.target_api.data = "/"
            result = maven_search(group=group,
                                  artifact=artifact,
                                  version=version,
                                  extension=extension)
            kwargs["result"] = result
            log.info("Posting to : %s", form.target_api.data)
            return render_template("index.html", **kwargs)

        elif form.submit_new.data:
            form.target_api.data = "/api/nexus/search"
            log.info("Posting to : %s", form.target_api.data)
            return redirect(url_for('search_artifact'),
                            group=group,
                            artifact=artifact,
                            version=version,
                            extension=extension)
    return render_template('index.html', **kwargs)


@app.route('/api/nexus/search/', methods=['get', 'post'])
def search_artifact():
    group = request.form.get('group')
    artifact = request.form.get('artifact')
    version = request.form.get('version')
    extension = request.form.get('extension')
    display_ca_bundle()
    return maven_search(group=group,
                        artifact=artifact,
                        version=version,
                        extension=extension)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
