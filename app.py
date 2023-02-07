import os

import flask
from flask import Flask, render_template

app = Flask(__name__,
            template_folder="/home/justin/apps/tic-tac-toe2/build",
            static_url_path="/home/justin/apps/tic-tac-toe2/build/static",
           )

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/static/<path:path>")
def static_files(path):
    return flask.send_from_directory("/home/justin/apps/tic-tac-toe2/build/static", path)