Flask-Collect-Invenio
#####################

.. _description:

**Flask-Collect-Invenio** is a fork and drop-in replacement of the original
**Flask-Collect** extension with adjustments to make it compatible with Flask 2.x.

Even though serving static files with *Flask* is a bad idea in a production
environment, this tool will help you collect them in one command.
It checks application and blueprints for static files and copies them to a
specific folder (saves related paths).

.. _badges:

.. image:: https://img.shields.io/pypi/v/flask-collect-invenio.svg?style=flat-square
    :target: https://pypi.python.org/pypi/flask-collect-invenio
    :alt: Version

.. image:: https://img.shields.io/pypi/dm/flask-collect-invenio.svg?style=flat-square
    :target: https://pypi.python.org/pypi/flask-collect-invenio
    :alt: Downloads

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


.. _documentation:

**Docs are available at** http://flask-collect-invenio.readthedocs.org/. **Pull
requests with documentation enhancements and/or fixes are awesome and most
welcome.**

.. _contents:

.. contents::


.. _requirements:

Requirements
=============

- Python 3.6+
- Flask_ >= 0.10.1


.. _installation:

Installation
============

**Flask-Collect-Invenio** should be installed using pip: ::

    pip install Flask-Collect-Invenio


.. _setup:

Setup
=====

Flask-Collect-Invenio settings (default values): ::

    # Target static dir
    COLLECT_STATIC_ROOT = <APP.ROOT_PATH>/static
    COLLECT_STORAGE = 'flask_collect.storage.file'

Initialize Flask-Collect-Invenio extension: ::

    from flask_collect import Collect

    ...

    collect = Collect()
    collect.init_app(app)

If you use Flask-Script_, activate Flask-Collect-Invenio commands: ::

    from flask_collect import Collect

    ...
    manager = Manager()
    ...

    collect = Collect()
    collect.init_app(app)
    collect.init_script(manager)

If you configure Flask via a factory function::

    from flask_collect import Collect

    ...

    def create_app():
        app = Flask()
        ...
        collect = Collect()
        collect.init_app(app)

        return app


.. _usage:

Use Flask-Collect-Invenio
=========================

From any python script: ::

    collect.collect(verbose=True)

with Flask-Script_: ::

    $ ./manage.py collect

with Flask>=0.11: ::

    $ flask collect


.. _bugtracker:

Bug tracker
===========

If you have any suggestions, bug reports or annoyances please report them
to the issue tracker at https://github.com/inveniosoftware/Flask-Collect-Invenio/issues


.. _contributing:

Contributors
============

Original Author: Kirill Klenov (horneds@gmail.com)

Also see the `CONTRIBUTORS.rst
<https://github.com/inveniosoftware/Flask-Collect-Invenio/blob/develop/CONTRIBUTORS.rst>`_
file.

Contributing
============

Development of flask-collect-invenio happens at github:
https://github.com/inveniosoftware/Flask-Collect-Invenio


.. _license:

License
=======

Licensed under a `BSD license`_.


.. _links:

.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: http://klen.github.com/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Flask: http://flask.pocoo.org/
.. _Flask-Script: http://github.com/rduplain/flask-script
