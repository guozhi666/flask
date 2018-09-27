from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/feedback/')
def feedbake():
    return render_template('post.html')

@app.route('/admin/edit/<id>/')
def edit():
    return render_template("edit.html")
if __name__ == '__main__':
    app.run()
