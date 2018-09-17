from flask import Flask, render_template
from flask import request
from urllib.parse import unquote
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg/')
def reg():

    return render_template('reg.html')
@app.route('/rq/')
def get_request():
    path = request.path
    #method = request.method
    name = unquote(request.args.get('name', 'no found'))
    return name

if __name__ == '__main__':
    app.run(debug=True)