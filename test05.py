# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:test05.py
# time:2021/7/28 17:34
from flask import Flask, Response, jsonify


app = Flask(__name__)


# 将试图函数中返回的字典，转换成json对象，然后返回
class JSONResponse(Response):


    @classmethod
    def force_type(
        cls, response: "Response", environ: t.Optional["WSGIEnvironment"] = None
    ) -> "Response":
        pass
