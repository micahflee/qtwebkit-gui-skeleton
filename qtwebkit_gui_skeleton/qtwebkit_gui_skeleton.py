import os, sys, threading, socket
import webapp

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

def choose_port():
    tmpsock = socket.socket()
    tmpsock.bind(("127.0.0.1", 0))
    port = tmpsock.getsockname()[1]
    tmpsock.close()
    return port

def launch_window(port):
    app = QApplication(sys.argv)
    web = QWebView()
    web.load(QUrl("http://127.0.0.1:{0}".format(port)))
    web.show()
    sys.exit(app.exec_())

def main():
    port = choose_port()

    # start the web app in a background thread
    t = threading.Thread(target=webapp.app.run, kwargs={'port':port})
    t.daemon = True
    t.start()

    # launch the window
    launch_window(port)

if __name__ == '__main__':
    main()
