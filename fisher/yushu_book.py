
from http import HTTP

class YuShuBook:
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/searvh?q={}&count={}&start={}'

    @classmethod
    def search_by_ibsn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result
    @classmethod
    def search_by_keyword(cls, keyword, count = 15, start = 0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result