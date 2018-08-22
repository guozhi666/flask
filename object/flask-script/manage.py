from flask_script import Manager
from app import app
import sqlite3
from models import User
manager = Manager(app)
@manager.command
def hello():
    print "hello"
@manager.option('-m', '--msg', dest = 'msg_val', default='world')
def hello_world(msg_val):
    print 'hello' + msg_val
@manager.command()
def init_db():
    sql = 'creat table user (id INT, name TEXT)'
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
if __name__ =="__main__":
    manager.run()