# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:test03.py
# time:2021/7/27 18:05
from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route("/login/")
def login_one():
    return "登录页面"


@app.route('/profile/')
def profile():
    if request.args.get("name"):
        return "个人中心"
    else:
        # print(url_for("login_one"))
        return redirect(url_for("login_one"))


if __name__ == "__main__":
    app.run(debug=True)
