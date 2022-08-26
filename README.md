# Data Visualization
A beginner tutorial to implement a simple data visualization web using `python flask` and `javascript Highcharts`.

## Requirements
The required library to run the repository in your local machine:
1. [python3](https://www.python.org/downloads/)
2. [pip3](https://www.activestate.com/resources/quick-reads/how-to-install-and-use-pip3/)
3. [python3 virtualenv](https://virtualenv.pypa.io/en/latest/)

Make sure you have `python3` and the two modules `pip3` and `virtualenv` by running the following commands in your command line or terminal.
```
$ python3 --version
Python 3.x.x
```

```
$ python3 -m pip --version
pip x.x.x from /pip/path
```

```
$ python3 -m pip install virtualenv #INSTALL virtualenv
$ python3 -m virtualenv --version
virtualenv x.x.x from /virtualenv/path
```

After making sure we have the main requirements. We need to create a virtualenv so we can download our own libraries separately from the global `python3` environment.
```
$ python3 -m virtualenv VENV_NAME
```

```
#Activate the virtualenv
$ VENV_NAME\Scripts\activate
```
After activating your virtualenv the `VENV_NAME` will appear at the beginning of the command line.

```
(VENV_NAME)$ YOUR_COMMAND_LINE
```

The `requirements.txt` file in the repository contains the python3 required libraries.

```
$ python3 -m pip -r install requirements.txt
```

## Run

```
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
$ set FLASK_DEBUG=1
$ flask run
```