# -*- coding: utf-8 -*-
#
# This file is part of Flask-Collect-Invenio.
# Copyright (C) 2012 - 2016 Kirill Klenov.
# Copyright (C) 2021        TU Wien.
#
# Flask-Collect-Invenio is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

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
