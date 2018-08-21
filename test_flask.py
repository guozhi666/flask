from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello world'

@app.route('/user', methods = ['POST'])
def hello_user():
	return 'hello user'

@app.route('/users/<id>')
def user_id(id):
	return 'hello user:' + id

@app.route('/query_user')
def query_user():
	id = request.args.get('id')
	return 'hello query:'+id


if __name__=='__main__':
	app.run()