#!/usr/bin/env python

import cgi

# Parse form inputs
form = cgi.FieldStorage()

print "Content-Type: text/html"

print "<html><head><title>Info</title></head><body>\n"

if "birthdate" in form:
    birthdate = form.getvalue('birthdate')
    print "<h3>Birthdate: " + birthdate + "</h3></br>"

if "hobby" in form:
    hobby = form.getvalue('hobby')
    print "<h3>Hobby: " + hobby + "</h3></br>"

print """<form method="post" action="hobbies.py">
    Name: <input type="text" value="name"><br/>
    Family: <input type="text" value="family"><br/>
    <input type="submit" value="Submit">
</form>
"""

print "</body></html>"
