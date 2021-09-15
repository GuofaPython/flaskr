# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:test02.py
# time:2021/7/27 11:14
from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class TelephoneConverter(BaseConverter):
    regex = r"1[38809]\d{9}"


# 用户访问/post/a+b
class ListConverter(BaseConverter):
    def to_python(self, value):
        # return 'hello'
        return value.split('+')

    def to_url(self, value):
        print(value)
        return "+".join(value)


app.url_map.converters['tel1'] = TelephoneConverter
app.url_map.converters['tel2'] = ListConverter


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    print("用户id：%s" % user_id)
    return "用户id：%s" % user_id


@app.route('/posts/<list:bords>/')
def posts(bords):
    print(bords)
    return "提交的版本：%s" % bords


if __name__ == "__main__":
    app.run(debug=True)
