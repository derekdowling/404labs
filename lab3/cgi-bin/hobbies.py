#!/usr/bin/env python

import cgi

# Parse form inputs
form = cgi.FieldStorage()

print "Content-Type: text/html"

print "<html><head><title>Hobbies</title></head><body>\n"

if "name" in form:
    name = form.getvalue('name')
    print "<h3>Name: " + name + "</h3></br>"

if "family" in form:
    family = form.getvalue('family')
    print "<h3>Family: " + family + "</h3></br></br>"

print """
<form method="post" action="info.py">
    Birthdate: <input type="text" value="birthdate"><br/>
    Main Hobby: <input type="text" value="hobby"><br/>
    <input type="submit" value="Submit">
</form>
"""

print "</body></html>"
