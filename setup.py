#!/usr/bin/env python
# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

from syn import __appname__, __version__
from setuptools import setup

long_description = open('README.md').read()

setup(
    name       = __appname__,
    version    = __version__,
    packages   = ['syn'],

    author       = "Paul Tagliamonte",
    author_email = "paultag@ubuntu.com",

    long_description = long_description,
    description      = 'Syn Package Manager',
    license          = "Expat",
    url              = "https://github.com/paultag/syn",

    platforms        = ['any']
)
