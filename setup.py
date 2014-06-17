#!/usr/bin/env python

import os, sys, platform

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = open('version').read().strip()
args = {}

if platform.system() == 'Darwin':
    args['data_files'] = ['LICENSE', 'README.md', 'version', 'qtwebkit_gui_skeleton']
    args['app'] = ['install/qtwebkit-gui-skeleton-osx.py']
    args['options'] = {
        'py2app': {
            'argv_emulation': True,
            'iconfile': 'install/icon.icns',
            'packages': ['flask'],
            'site_packages': True,
            'plist': {
                'CFBundleName': 'QtWebkitGUISkeleton',
            }
        }
    }

elif platform.system() == 'Windows':
    pass

else:
    pass

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
    include_package_data=True,
    **args
)
