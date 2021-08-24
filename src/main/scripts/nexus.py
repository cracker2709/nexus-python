#!/usr/bin/env python3
import os

from werkzeug.utils import redirect

from NexusForm import NexusForm
from nexus_tools import maven_search, display_ca_bundle
from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder='templates')

api = "/service/rest/v1/search/assets"

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
@app.route("/index.html")
@app.route("/statics/img/html")
def index():
    form = NexusForm()
    if form.validate_on_submit():
        group = form.group.data
        artifact = form.atrifact.data
        version = form.version.data
        extension = form.extension.data
        return redirect(url_for('maven_search'),
                        group=group,
                        artifact=artifact,
                        version=version,
                        extension=extension)

    return render_template('index.html', logo="static/img/nexus-logo.png",
                           wallpaper="static/img/wallpaper.jpg", form=form)


@app.route('/api/nexus/search/', methods=['post'])
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
