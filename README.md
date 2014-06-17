# qtwebkit-gui-skeleton

A skeleton project for making cross-platform GUI desktop apps that are powered by Qt4, webkit, and flask.

## Working in a virtual environment

    virtualenv env
    . env/bin/activate
    python setup.py sdist
    pip install dist/qtwebkit-gui-skeleton-`cat version`.tar.gz

## Mac OS X

Make sure python looks for modules in `/usr/local/lib/python2.7/site-packages/`:

    echo export PYTHONPATH=\$PYTHONPATH:/usr/local/lib/python2.7/site-packages/ >> ~/.profile
    source ~/.profile

Install qt5 and pyqt with homebrew:

    brew install qt4 pyqt

