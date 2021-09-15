# !/usr/bin/env python
# encoding:utf-8
# author: George.Z
# file:test007.py
# time:2021/8/9 17:12


from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD']


@app.route('/')
def index():
    context = {
        'position':-9,
        'singature': 1,
        'article': 'hello zhiliao world'
    }