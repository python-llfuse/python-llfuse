..
  NOTE: We cannot use sophisticated ReST syntax (like
  e.g. :file:`foo`) here because this isn't rendered correctly
  by PyPi.

The Python-LLFUSE Module
========================


.. start-intro

**Warning - no longer maintained**

Python-LLFUSE is no longer actively maintained. Unless you are stuck
with Python 2.x or libfuse 2.x, we recommended to use the pyfuse3_
module instead.

Python-LLFUSE is a set of Python bindings for the low level FUSE_
API. It requires at least FUSE 2.8.0 and supports both Python 2.x and
3.x. Like FUSE itself, Python-LLFUSE is developed for Linux systems,
but it should be compatible with OS-X, FreeBSD and NetBSD as well.

Python-LLFUSE releases can be downloaded from PyPi_. The documentation
can be `read online`__ and is also included in the ``doc/html``
directory of the Python-LLFUSE tarball.


.. _pyfuse3: https://github.com/libfuse/pyfuse3

Getting Help
------------

Please report any bugs on the `issue tracker`_. For discussion and
questions, please use the general `FUSE mailing list`_. A searchable
`mailing list archive`_ is kindly provided by Gmane_.


Contributing
------------

The Python-LLFUSE source code is available on GitHub_.


.. __: http://www.rath.org/llfuse-docs/
.. _FUSE: http://github.com/libfuse/libfuse
.. _FUSE mailing list: https://lists.sourceforge.net/lists/listinfo/fuse-devel
.. _issue tracker: https://github.com/python-llfuse/python-llfuse/issues
.. _mailing list archive: http://dir.gmane.org/gmane.comp.file-systems.fuse.devel
.. _Gmane: http://www.gmane.org/
.. _PyPi: https://pypi.python.org/pypi/llfuse/
.. _GitHub: https://github.com/python-llfuse/python-llfuse
