#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer
import cgitb

# This line enables CGI error reporting
cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)

# handler.cgi_directories = ["/cg]

httpd = server(server_address, handler)
httpd.serve_forever()
