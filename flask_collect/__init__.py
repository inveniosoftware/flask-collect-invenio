# -*- coding: utf-8 -*-
"""
**Flask-Collect** is an extension for Flask that helps collecting static files.

Serving static files with *Flask* -- bad idea for production, this tool will
help you collect them in one command. It checks application and blueprints for
static files and copy them to specific folder (saves related paths).
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
