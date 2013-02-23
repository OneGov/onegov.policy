onegov.policy
=============

`onegov.policy`, the policy package for `OneGov Box`_ pulls together and configures the
OneGov modules.


.. contents:: Table of Contents


Installing OneGov
-----------------

For details on how to install `OneGov Box`_ see the instructions in the readme of the
`onegov-buildout <https://github.com/OneGov/onegov-buildout/>`_.


Development
-----------

For development, you can install the onegov.policy package directly (without using the onegov-buildout):

.. code::shell

    $ git clone https://github.com/OneGov/onegov.policy.git
    $ cd onegov.policy
    $ ln -s development.cfg buildout.cfg
    $ python2.7 bootstrap.py
    $ bin/buildout
    $ bin/instance fg


Links
-----

- Buildout: https://github.com/OneGov/onegov-buildout
- Source: https://github.com/OneGov/onegov.policy
- Issue tracker: https://github.com/OneGov/onegov.policy/issues


Copyright
---------

This package is copyright by `Verein OneGov <http://www.onegov.ch/>`_.

``onegov.policy`` is licensed under GNU General Public License, version 2.


.. _OneGov Box: http://www.onegov.ch/
