import os
import configparser
import pandas as pd

from constants import WEB_PAGE, TITLE, DATA, DATASET_NAME
from charts import Charts

from flask import Flask, render_template


app = Flask(__name__)

# Read the configuration.ini file
config = configparser.ConfigParser()
config.read(
    os.path.join(
        os.getcwd(), 'configurations.ini'
    )
)

# Read the dataset
data_frame = pd.read_csv(
    os.path.join(
        os.getcwd(), config[DATA][DATASET_NAME]
    )
)

# Initilize the Charts object 
charts_object = Charts(data_frame)


@app.errorhandler(404)
def error_route(e):
    return render_template(
        '404.html',
        title=config[WEB_PAGE][TITLE],
    )

@app.route("/")
def main():  
    return render_template(
        'index.html',
        title=config[WEB_PAGE][TITLE],
        charts=charts_object.charts_data
    )

if __name__ == '__main__':
    app.run(debug=True)