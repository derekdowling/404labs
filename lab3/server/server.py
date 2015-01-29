#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer
import cgitb
import os

# This line enables CGI error reporting
cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)

rel_dir = os.path.dirname(__file__)
cgi_path = os.path.join(rel_dir, '/cgi-bin')
print cgi_path

handler.cgi_directories = [cgi_path]

httpd = server(server_address, handler)
httpd.serve_forever()
