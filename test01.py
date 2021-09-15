# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:test01.py
# time:2021/7/27 11:10
from flask import Flask, config, request, url_for
import uuid
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.debug = True


class TelephoneConverter(BaseConverter):
    regex = r"1[38809]\d{9}"


class ListConverter(BaseException):
    def to_python(self, value):
        return "hello"

    def to_url(self, value):
        return "hello"


app.url_map.converters['tel1'] = TelephoneConverter
app.url_map.converters['tel2'] = ListConverter


@app.route('/telephone/<tel1:my_tel>/')
def my_tel(my_tel):
    return "手机号：%s" % my_tel

# @app.route('/')
# def hello():
#     return 'hello'


# print(uuid.uuid4())
#
#
# @app.route('/u//<uuid:user_id>/')
# def user_detail(user_id):
#     return "用户中心页面:%s" % user_id
# @app.route('/<any(blog,user):url_path>/<id>')
# def detail(url_path, id):
#     if url_path == 'blog':
#         return "博客详情:%s" % id
#     else:
#         return "用户详情：%s" % id
# @app.route('/d/')
# def d():
#     wd = request.args.get('wd')
#     return "查询字符串:%s" % wd
# @app.route('/')
# def hello():
# return "hello"
# @app.route("/post/list/<page>/")
# def my_lsit(page):
#     print(page)
#     return url_for("my_lsit", page=page, count=2)


# @app.route('/list/')
# def article_List():
#     return 'article_list'


if __name__ == "__main__":
    app.run(debug=True)
