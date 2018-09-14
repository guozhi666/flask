# -*- coding:utf-8 -*-
from flask import Flask, request, make_response, render_template, redirect
from flask import url_for, abort
import json

app = Flask('__name__')

@app.route('/')
def index():
    resp = make_response()
    resp.response = render_template('index.html')  #返回内容
    resp.headers['content-type'] = 'text/html'     #响应头部信息字典表
    resp.status_code = 200                         #响应状态码
    return resp

@app.route('/a/')
def rq_a():
    #return redirect('/b/')              # 301 永久转跳     302临时转跳
    #return redirect(url_for('rq_b'))    # 301 永久转跳     302临时转跳
    return render_template('page-a.html')

@app.route('/help/')
def req_help():
    abort(404)


@app.route('/about/')
def rq_b():
    return render_template('page-b.html')


@app.route('/rq/')
def test_rq():
    data = {}
    data['ip'] = request.remote_addr
    data['full_path'] = request.full_path
    data['url'] = request.url
    data['is_xhr'] = request.is_xhr
    data['endpoint'] = request.endpoint
    return str(data)


@app.route('/user/')
def user_info():
    name = 'Tom'
    return render_template('user_info.html', name = name)


if __name__ =='__main__':
    app.run()