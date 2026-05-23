# SPDX-FileCopyrightText: 2012-2016 Kirill Klenov.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-License-Identifier: BSD-3-Clause

"""
**Flask-Collect-Invenio** is an extension for Flask that helps collecting static files.

Even though serving static files with *Flask* is a bad idea in a production
environment, this tool will help you collect them in one command.
It checks application and blueprints for static files and copies them to a
specific folder (saves related paths).
"""

from .collect import Collect
from .version import __version__

__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "BSD"
__project__ = __name__

__all__ = (
    "Collect",
    "__author__",
    "__license__",
    "__project__",
    "__version__",
)
