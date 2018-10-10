#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copied from the flask project's setup.py

import io
import re
from collections import OrderedDict

from setuptools import setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('bestpractices/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='bestpractices',
    version=version,
    url='https://github.com/allentsouhuang/bestpractices',
    project_urls=OrderedDict((
        ('Code', 'https://github.com/allentsouhuang/bestpractices'),
    )),
    license='BSD',
    author='Allen Huang',
    author_email='',
    maintainer='Allen Huang',
    maintainer_email='contact@palletsprojects.com',
    description='A reference for best practices in python.',
    long_description=readme,
    packages=['bestpractices'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=3',
            'coverage',
            'tox',
            'sphinx',
        ],
        'docs': [
            'sphinx',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [],
    },
)
