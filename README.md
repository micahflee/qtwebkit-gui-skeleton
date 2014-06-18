# qtwebkit-gui-skeleton

A skeleton project for making cross-platform GUI desktop apps that are powered by Qt4, webkit, and flask.

## Windows

The first time you're setting up your dev environment:

* Download and install the latest python 2.7 from https://www.python.org/downloads/ -- make sure you install the 32-bit version.
* Right click on Computer, go to Properties. Click "Advanced system settings". Click Environment Variables. Under "System variables" double-click on Path to edit it. Add `;C:\Python27;C:\Python27\Scripts` to the end. Now you can just type `python` to run python scripts in the command prompt.
* Go to https://pip.pypa.io/en/latest/installing.html. Right-click on `get-pip.py` and Save Link As, and save it to your home folder.
* Open `cmd.exe` as an administrator. Type: `python get-pip.py`. Now you can use `pip` to install packages.
* Go to http://www.riverbankcomputing.com/software/pyqt/download and download the latest PyQt4 for Windows for python 2.7, 32-bit (I downloaded `PyQt4-4.11-gpl-Py2.7-Qt4.8.6-x32.exe`), then install it.
* Go to http://www.py2exe.org/ and download the latest py2exe for python 2.7, 32-bit (I downloaded `py2exe-0.6.9.win32-py2.7.exe`), then install it.
* Open a command prompt and cd into the qtwebkit-gui-skeleton folder and type: `pip install flask`
* Go to `C:\Python27\Lib\site-packages\flask\` and delete the folder `testsuite`. This is necessary to work around a py2exe bug.
* Open a command prompt, cd to the qtwebkit-gui-skeleton folder, and type: `python setup.py py2exe`. This will create a ton of files in `dist`, including `qtwebkit-gui-skeleton.exe`.

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
