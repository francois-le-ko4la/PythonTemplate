#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A setuptools based setup module.

Example:
    ./python test
    ./python install

Test:
    This script has been tested and validated on Ubuntu.
    pylint has been used :
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

Note:
    This script is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 3 of the License, or (at your option) any later version.

    This script is provided in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

from setuptools import setup


def readme():
    """This function provides the readme file.
    """
    with open('README.md') as read_me:
        return read_me.read()


setup(
    name='myname',
    version='0.1',
    description='description',
    long_description=readme(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3.6',
        'Topic :: REST API :: Social Network / Cloud',
        ],
    url='https://github.com/XXXXX.git',
    author='xxx',
    author_email='xwwww',
    license='GPL3',
    packages=['mypackage'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite="tests.XXXX",
    zip_safe=False
    )
