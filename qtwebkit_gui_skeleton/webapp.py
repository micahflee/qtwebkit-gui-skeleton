import os, sys, json
from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')

# log errors to syslog
import logging
log_handler = logging.FileHandler('/tmp/qtwebkit-gui-skeleton.log')
log_handler.setLevel(logging.WARNING)
app.logger.addHandler(log_handler)

@app.route("/")
def index():
    return render_template('index.html')

