# SPDX-FileCopyrightText: 2012-2016 Kirill Klenov.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-License-Identifier: BSD-3-Clause

import os
import re
import datetime

# Get the version string.  Cannot be done with import!
g = {}
with open(os.path.join('..', 'flask_collect', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g["__version__"]

# The full version, including alpha/beta/rc tags.
release = version
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Flask-Collect-Invenio'
copyright = u'%s, Kirill Klenov' % datetime.datetime.now().year
exclude_patterns = ['_build']
htmlhelp_basename = 'Flask-Collect-Inveniodoc'
latex_documents = [
    ('index', 'Flask-Collect-Invenio.tex', u'Flask-Collect-Invenio Documentation',
        u'Kirill Klenov', 'manual'),
]
latex_elements = {}
man_pages = [
    ('index', 'flask-mixer', u'Flask-Collect-Invenio Documentation',
     [u'Kirill Klenov'], 1)
]
pygments_style = 'sphinx'
html_theme = 'alabaster'
html_theme_options = {}
