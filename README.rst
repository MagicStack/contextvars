PEP 567 Backport
================

This package implements a backport of Python 3.7 ``contextvars``
module (see PEP 567) for Python 3.6.

**Important:** at this moment this package does not provide an
asyncio event loop with PEP 567 support yet.  Stay tuned for updates.

Documentation: https://docs.python.org/3.7/library/contextvars.html

Usage:

.. code-block:: python

    try:
        import contextvars
    except ImportError:
        import pep567 as contextvars

    my_var = contextvars.ContextVar('my_var')
    # ...


License
=======

Apache 2.0.
