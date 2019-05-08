# encoding: utf8
from flask import Flask, request, Response, render_template, redirect, url_for
import json, datetime, time, urllib, urllib2
import sys, os
reload(sys)
sys.setdefaultencoding('utf-8') 

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(seconds=1)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html',message="")

@app.route('/save',methods=['POST'])
def writefile():
    filename = request.form.get('filename', None)
    text = request.form.get('text', None)
    if filename is None or text is None:
        return render_template('index.html',message="参数输入有误。")
    with open(filename,"w") as f: f.write(text)
    return render_template('index.html',message="保存成功。")


