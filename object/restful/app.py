from flask import Flask, request, redirect
import base64
import time
from flask.ext import restful
app = Flask(__name__)

user = {
    "magigo": ['123456']
}
client_id = '123456'

def gen_token(uid):
    token = base64.b64encode

def verify_token():
    pass
@app.route('/index/<user>', methods = ['POST'])
def hello_world(user):
    return 'Hello %s' % user

@app.route('/login', methods = ['POST'])
def login():
    pass

@app.route('/test', methods = ['POST'])
def test():
    pass

if __name__ == '__main__':
    app.run(debug=True)
