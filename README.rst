.. image:: https://travis-ci.org/MagicStack/pep567.svg?branch=master
    :target: https://travis-ci.org/MagicStack/pep567


PEP 567 Backport
================

This package implements a backport of Python 3.7 ``contextvars``
module (see PEP 567) for Python 3.6.

**Important:** at this moment this package does not provide an
asyncio event loop with PEP 567 support yet.  Stay tuned for updates.


Documentation
=============

Read the official ``contextvars`` module documentation here:
https://docs.python.org/3.7/library/contextvars.html


`PEP 567 <https://www.python.org/dev/peps/pep-0567/>`_ also provides
a comprehensive overview of the API and explains the design choices.


Installation
============

.. code-block:: bash

    $ pip install pep567


Usage
=====

.. code-block:: python

    try:
        # Python 3.7
        import contextvars
    except ImportError:
        # Python <= 3.6
        import pep567 as contextvars

    my_var = contextvars.ContextVar('my_var')
    # ...


License
=======

Apache 2.0.
