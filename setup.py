#!/usr/bin/env python

import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = open('version').read().strip()

setup(
    name='qtwebkit-gui-skeleton',
    version=version,
    description='A skeleton project for making cross-platform GUI desktop apps that are powered by Qt4, webkit, and flask.',
    long_description="""A skeleton project for making cross-platform GUI desktop apps that are powered by Qt4, webkit, and flask.""",
    author='Micah Lee',
    author_email='micah@micahflee.com',
    url='https://github.com/micahflee/qtwebkit-gui-skeleton',
    license="GPL v2",
    install_requires=[
        'flask >= 0.8'
    ],
    packages=['qtwebkit_gui_skeleton'],
    include_package_data=True
)
