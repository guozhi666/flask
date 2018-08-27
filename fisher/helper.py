# -*- coding:utf-8 -*-

def is_isbn_or_key(word):
    #用来判断 word 是关键字还是isbn
    isbn_or_key = 'key'
    if len(word) ==13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '_' in word and len(word.replace('_', '')) == 10 and word.replace('_', '').isdigit:
        isbn_or_key = 'isbn'

    return isbn_or_key