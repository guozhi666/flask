from datetime import datetime
import sqlite3
from flask import Flask,render_template,request,redirect

app = Flask(__name__)
app.debug = True

DATEBASE_URL = r'.db/feedback.db'
@app.route('/')
def hello_word():
    return render_template('base.html')

@app.route('/feedback/')
def feedback():
    conn = sqlite3.connect(DATEBASE_URL)
    c = conn.cursor()

    sql = 'select ROWID,CategoryName from category'
    categories = c.execute(sql).fetchall()
    c.close()
    conn.close()
    return render_template('post.html',categories = categories)

@app.route('/post_feedback/',methods=['POST'])
def post_feedback():
    if request.method == 'POST':
        subject = request.form['subject']
        categoryid = request.form.get('category', 1)
        username = request.form.get('username')
        email = request.form.get('eamil')
        body = request.form.get('body')
        release_time = datetime.now()
        is_processed = 0

        conn = sqlite3.connect(DATEBASE_URL)
        c = conn.cursor()
        sql = "insert into feedbackss (Subject,CategoryID, Username, EMAIL, Body, IsProcessed, ReleaseTime) values(?, ?, ?, ?, ?, ?, ?)"
        c.execute(sql,(subject, categoryid, username, email, body, is_processed, release_time))
        conn.commit()
        conn.close()
        return redirect(url_for('feedback'))

@app.route('/admin/list/')
def feedback_list():
    conn = sqlite3.connect(DATEBASE_URL)
    c = conn.cursor()
    sql = 'select ROWID,* from feedbackss ORDER BY ROWIN DESC'
    feedbacks = c.execute(sql).fetchall()
    conn.close()
    return render_template('feedback-list.html', items = feedbacks)

if __name__ == '__main__':
    app.run()