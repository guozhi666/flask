# -*- coding:utf-8 -*-

from flask import Flask, render_template
from models.book import Book

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def book_list():
    books = [
        Book('python Flaks', '49.00', 'guozhi', '人民邮电出版社'),
        Book('python', '59.00', 'guozhi', '人民邮电出版社'),
        Book('高等数学', '39.00', 'guozhi', '人民邮电出版社'),
        Book('大学物理', '29.00', 'guozhi', '人民邮电出版社'),
        Book('大学物理', '29.00', 'guozhi', '人民邮电出版社'),
        Book('线性代数', '19.00', 'guozhi', '人民邮电出版社')
    ]
    #book = Book('python Flaks', '49.00', 'guozhi', '人民邮电出版社')
    return render_template('book-list.html', book = books)

if __name__ == "__main__":
    app.run()