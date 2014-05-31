#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#  
#  Copyright 2014 Eduardo Echeverria <echevemaster@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import os
import subprocess

from setuptools import setup

PUBLISH_CMD = 'python setup.py register sdist upload'
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist upload -r test'

if 'publish' in sys.argv:
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit()


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='kickstart-fedora-online',
    version='0.1.0',
    description='Fedora iso creator online.'
    long_description=read('README.md'),
    author='Valentin Basel, Eduardo Echeverria',
    author_email='valentinbasel@fedoraproject.org | echevemaster@gmail.com',
    url='https://github.com/proyectofedora-infra/kickstart-fedora-online',
    install_requires=['Flask', 'pykickstart'],
    license=read('LICENSE'),
    zip_safe=False,
    packages=['kickstart'],
    keywords='kickstart, fedora, iso',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'kickstart = kickstart:main'
        ]
    }
)
