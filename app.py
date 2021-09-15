# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:app.py.py
# time:2021/6/2511:10


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=)
    app.config.from_object("config")
