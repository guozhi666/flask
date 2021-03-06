#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:guozhi@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
#会员
class User(db.Modil):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True )
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True)
    userlogs = db.relation('Userlog', backref = 'user')
    def __repr__(self):
        return "<User %r>" %self.name

class Userlog(db.Model):
    __tablename__="username"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id