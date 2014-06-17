# qtwebkit-gui-skeleton

A skeleton project for making cross-platform GUI desktop apps that are powered by Qt4, webkit, and flask.

## Mac OS X

The first time you're setting up your dev environment:

    echo export PYTHONPATH=\$PYTHONPATH:/usr/local/lib/python2.7/site-packages/ >> ~/.profile
    source ~/.profile
    brew install qt4 pyqt
    virtualenv env
    . env/bin/activate
    pip install flask
    pip install py2app
    # fixes a silly bug https://bitbucket.org/ronaldoussoren/py2app/issue/143/resulting-app-mistakenly-looks-for-pyside
    patch env/lib/python2.7/site-packages/py2app/util.py < py2app.patch

Each time you start work:

    . env/bin/activate

Build the .app:

    python setup.py py2app

Now you should have `dist/QtWebkitGUISkeleton.app`.
