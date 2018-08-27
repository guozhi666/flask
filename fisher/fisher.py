#-*- coding:utf-8 -*-
#  api  https://api.douban.com/v2/book/isbn/9787111521181


from flask import Flask
#from config import DEBUG   #引用配置文件的第一种方法


app = Flask(__name__)
app.config.from_object('config')  #引用配置文件的第二种方法

if __name__ == '__main__':
    app.run()