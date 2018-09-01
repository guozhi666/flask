import cgi

form = cgi.FieldStorage()
print('Content-type: text/html\n')

#name = "未获取"
#if 'username' in form:
   # name = form ['username'].value
name = form['username'].value if 'username'in form else "unkonw"

print ('<h1>hello {}</h1>'.format(name))
