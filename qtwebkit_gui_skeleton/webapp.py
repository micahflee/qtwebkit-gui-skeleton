import os, sys, json, platform
from flask import Flask, render_template

# figure out this platform's temp dir
if platform.system() == 'Windows':
    temp_dir = os.environ['Temp'].replace('\\', '/')
else:
    temp_dir = '/tmp/'

# suppress output in windows
if platform.system() == 'Windows':
    sys.stdout = open('{0}/qtwebkit-gui-skeleton.stdout.log'.format(temp_dir), 'w')
    sys.stderr = open('{0}/qtwebkit-gui-skeleton.stderr.log'.format(temp_dir), 'w')

# log web errors to file
import logging
log_handler = logging.FileHandler('{0}/qtwebkit-gui-skeleton.web.log'.format(temp_dir))
log_handler.setLevel(logging.WARNING)

app = Flask(__name__, template_folder='./templates')
app.logger.addHandler(log_handler)

@app.route("/")
def index():
    return render_template('index.html')

