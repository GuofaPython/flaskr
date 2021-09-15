# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:test006.py
# time:2021/8/2 10:50

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def hello_word():
    return render_template('index.html')


@app.route("/accounts/login/<id>/")
def login(id):
    print(id)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
