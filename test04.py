# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:test04.py
# time:2021/7/27 18:40
from flask import Flask, Response, jsonify
from werkzeug.wrappers import Response

app = Flask(__name__)


# 将视图函数中的返回字典，转化成json对象,然后返回
class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        print(response)
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)


# 添加response类， 一定要添加
app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return Response('hello', status=200, mimetype='text/html')


# 设置cookie
@app.route('/list1/')
def list1():
    resp = Response('list1')
    resp.set_cookie('miku', 'angle')
    return resp


# 添加响应头
@app.route('/list2/')
def list2():
    return 'list2', 200, {"X-NAME": "MIKU", "Server": "windows2003"}


# json, 非字符， 非元组
@app.route('/list3/')
def list3():
    return {"username": "miku", "age": 16}


if __name__ == "__main__":
    app.run(debug=True)
