#!/usr/bin/env python

import os, sys, platform
from glob import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def file_list(path):
    files = []
    for filename in os.listdir(path):
        if os.path.isfile(path+'/'+filename):
            files.append(path+'/'+filename)
    return files

version = open('version').read().strip()
args = {}

if platform.system() == 'Darwin':
    args['data_files'] = ['LICENSE', 'README.md', 'version']
    args['app'] = ['install/qtwebkit-gui-skeleton.py']
    args['options'] = {
        'py2app': {
            'argv_emulation': True,
            'packages': ['qtwebkit_gui_skeleton', 'flask', 'jinja2'],
            'includes': ['PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui', 'PyQt4.QtWebkit', 'PyQt4.QtNetwork', 'threading'],
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
    import py2exe
    args['windows'] = [{'script':'install/qtwebkit-gui-skeleton.py'}]
    args['data_files'] = [
        ('', ['LICENSE', 'README.md', 'version']),
        ('qtwebkit_gui_skeleton/templates', glob('qtwebkit_gui_skeleton/templates/*')),
        ('qtwebkit_gui_skeleton/static', glob('qtwebkit_gui_skeleton/static/*'))
    ]
    args['options'] = {
        'py2exe': {
            'includes': ['sip', 'PyQt4', 'PyQt4.QtNetwork'],
            'dll_excludes': ['MSVCP90.dll'],
            'packages': ['jinja2', 'flask'],
            'skip_archive': True
        }
    }

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
