virtual-less
============

This is a small package that installs the `less`_ compiler for CSS
into you virtual environment without the need of a global installation
or the node package manager. The package is based on `python-less`_ and
currently only installs the latest version of `less`_.

This package does not include `node.js`_ and does not specify it as a
requirement to be as flexible as possible. If you would like a similarly
easy installation of node into your ``virtualenv`` you can check out
`virtual-node`_.


.. _`less`: http://lesscss.org
.. _`python-less`: https://github.com/linssen/python-less
.. _`node.js`: http://nodejs.org/
.. _`virtual-node`: http://github.com/elbaschid/virtual-node


Installation
------------

Installing the ``lessc`` commandline compiler is as easy as::

    $ pip install virtual-less

that should be it. You should now be able to run the less compiler
in you shell. You can check where ``lessc`` is installed to confirm
that::

    $ which lessc
    /home/elbaschid/.virtualenvs/lessc-test/bin/lessc

Issues & Contributions
----------------------

Please let me know if you have any issues, please raise an issue
here on the github project.

If you want to contribute, fork this repository and open a pull
request with your changes. I'd be happy to include them.

License
-------

This package is released under the permissive `New BSD license`_.

.. _`New BSD license`: https://github.com/elbaschid/virtual-less/blob/master/LICENSE
