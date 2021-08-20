from pybuilder.core import use_plugin, init
from setuptools import find_packages
from setuptools.command.install import install
import xml.dom.minidom

# These are the plugins we want to use in our project.
# Projects provide tasks which are blocks of logic executed by PyBuilder.
use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a linter plugin that runs flake8 (pyflakes + pep8) on our project sources
use_plugin("python.flake8")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")

# The project name
doc = xml.dom.minidom.parse("pom.xml")
version = doc.getElementsByTagName("version")[0].childNodes[0].data

# Manage snapshots version
version = str(version).replace("-SNAPSHOT", ".dev")

name = str(doc.getElementsByTagName("artifactId")[0].childNodes[0].data)
version = str(version)
description = str(doc.getElementsByTagName("description")[0].childNodes[0].data)

install_requires = [
    "Jinja2",
    "jsonschema",
    "MarkupSafe",
    "openapi-schema-validator",
    "openapi-spec-validator",
    "pybuilder",
    "pycparser",
    "pyOpenSSL",
    "pyrsistent",
    "python-dateutil",
    "PyYAML",
    "requests",
    "requests-toolbelt",
    "six",
    "urllib3",
    "Werkzeug",
    "WTForms"
]
zip_safe = False
long_description = ''
long_description_content_type = None
classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python'
]
keywords = ''

author = 'Guillaume APCHAIN'
author_email = 'guillaume.apchain@gmail.com'
maintainer = ''
maintainer_email = ''

license = 'GAP'

url = '#'
project_urls = {}

scripts = [
    'scripts/nexus.py'
]
packages = find_packages(where=".")
namespace_packages = []
py_modules = ['__init__']
entry_points = {}
data_files = []
package_data = {}
dependency_links = []
cmdclass = {'install': install}
python_requires = ''
requires_dist = 'Jinja2,jsonschema,MarkupSafe,openapi-schema-validator,openapi-spec-validator,pybuilder,pycparser,' \
                'pyOpenSSL,pyrsistent,python-dateutil,PyYAML,requests,requests-toolbelt,six,urllib3,Werkzeug,WTForms '
obsoletes = []
platform = 'Linux'

# What PyBuilder should run when no tasks are given.
# Calling "pyb" amounts to calling "pyb publish" here.
# We could run several tasks by assigning a list to `default_task`.
default_task = "publish"


# This is an initializer, a block of logic that runs before the project is built.
@init
def set_properties(project):
    project.set_property("coverage_break_build", False)  # default is True
    project.build_depends_on("mock")
