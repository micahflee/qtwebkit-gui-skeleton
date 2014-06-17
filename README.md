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

## Debian-based Linux (Debian, Ubuntu, etc.)

The first time you're setting up your dev environment:'

    sudo apt-get install -y build-essential fakeroot python-all python-stdeb python-flask python-qt4
    ./build_deb.sh

Build and install the .deb:

    ./build_deb.sh
    sudo dpkg -i deb_dist/qtwebkit-gui-skeleton_*.deb

## RPM-based Linux (Red Hat, Fedora, CentOS)

The first time you're setting up your dev environment:'

    sudo yum install -y rpm-build python-flask python-stem pywebkitgtk

Build and install the .rpm:

    ./build_rpm.sh
    sudo yum install -y dist/qtwebkit-gui-skeleton-*.rpm

If you already have qtwebkit-gui-skeleton installed, you can reinstall with:

    sudo yum reinstall -y dist/qtwebkit-gui-skeleton-*.rpm
