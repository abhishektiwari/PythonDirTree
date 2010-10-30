#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of PythonDirTree.
#
# Files included in this package PythonDirTree are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.


try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
 
config = {
	'name' : 'mypackage',
	'description': 'Describes how import works in a Python project',
	'author': 'Abhishek Tiwari',
	'url': 'http://github.com/abhishektiwari/PythonDirTree',
	'download_url': 'http://github.com/abhishektiwari/PythonDirTree',
	'author_email': 'abhishek@abhishek-tiwari.com',
	'version': '0.1',
	'install_requires': ['ModuleName1','ModuleName1'],
	'packages': ['mypackage'],
	'scripts': [],
}

setup(**config)
