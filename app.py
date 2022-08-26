import os
import configparser

from constants import WEB_PAGE, TITLE

from flask import Flask, render_template

app = Flask(__name__)

# Read the configuration.ini file
config = configparser.ConfigParser()
config.read(
    os.path.join(
        os.getcwd(), 'configurations.ini'
    )
)

@app.errorhandler(404)
def error_route(e):
    return render_template(
        '404.html',
        title=config[WEB_PAGE][TITLE],
    )

@app.route("/")
def hello_world():
    return render_template(
        'index.html',
        title=config[WEB_PAGE][TITLE],
    )

if __name__ == '__main__':
    app.run(debug=True)