bootstrappy
===========

A Python program to generate a basic Python program. Whee

What does it do?
----------------

I made it for my own use, so it does what I do when I'm making a new
project:

-  Create a new directory in ~/workspace (if this directory doesn't
   exist it will probably error out)
-  Create the necessary boilerplate files for a module (readme,
   setup.py, module directory, **init** and **main**, module file at
   .py) in said directory

I then go in and put whatever code I want in module/module.py, add more
files if I like, making sure to populate main() as that's what is called
by the CLI handler. Then I can use ``python3 setup.py install`` to
install it systemwide.

Usage
-----

::

    usage: bootstrappy [-h] name desc deps

    positional arguments:
      name        Name of project
      desc        Description of project
      deps        Dependencies. Comma-separated list

    optional arguments:
      -h, --help  show this help message and exit

Installation
------------

-  Clone the repository, ``cd bootstrappy``
-  Run ``python3 setup.py install`` or ``pip3 install -e``
