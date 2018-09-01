import os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80

os.chdir(webdir)
server_address = ('', port)
server_obj = HTTPServer(server_address, CGIHTTPRequestHandler)
server_obj.serve_forever()