#!/usr/bin/env python

import os, sys, platform

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = open('version').read().strip()
args = {}

if platform.system() == 'Darwin':
    args['data_files'] = ['LICENSE', 'README.md', 'version']
    args['app'] = ['install/qtwebkit-gui-skeleton-osx.py']
    args['options'] = {
        'py2app': {
            'argv_emulation': True,
            'packages': ['flask', 'jinja2', 'qtwebkit_gui_skeleton'],
            'includes': ['PyQt4',' PyQt4.QtCore', 'PyQt4.QtGui', 'PyQt4.QtWebkit', 'PYQt4.QtNetwork', 'threading'],
            'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtOpenGL', 'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtXml', 'PyQt4.phonon'],
            'iconfile': 'install/icon.icns',
            'site_packages': True,
            'plist': {
                'CFBundleName': 'QtWebkitGUISkeleton',
            }
        }
    }
    args['setup_requires'] = 'py2app'

elif platform.system() == 'Windows':
    pass

else:
    args['packages'] = ['qtwebkit_gui_skeleton']
    args['include_package_data'] = True
    args['scripts'] = ['install/qtwebkit-gui-skeleton']
    args['data_files'] = [
        ('/usr/share/applications', ['install/qtwebkit-gui-skeleton.desktop']),
        ('/usr/share/pixmaps', ['install/qtwebkit-gui-skeleton.xpm'])
    ]

setup(
    name='qtwebkit-gui-skeleton',
    version=version,
    description='A skeleton project for making cross-platform GUI desktop apps that are powered by Qt4, webkit, and flask.',
    long_description="""A skeleton project for making cross-platform GUI desktop apps that are powered by Qt4, webkit, and flask.""",
    author='Micah Lee',
    author_email='micah@micahflee.com',
    url='https://github.com/micahflee/qtwebkit-gui-skeleton',
    license="GPL v2",
    **args
)
