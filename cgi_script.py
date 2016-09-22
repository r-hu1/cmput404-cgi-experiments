#!/usr/bin/env python

import cgi
import os
import json
import sys
form = cgi.FieldStorage()
loggedinok = False


if form.getvalue('user') == 'bob' and form.getvalue('password') == 'hunter2':
	loggedinok = True

if 'loggedin=true' in os.environ['HTTP_COOKIE']:
	loggedinok=True

print "Content-type: text/html"

if loggedinok:
	print "Set-Cookie: loggedin=true"

print
print "<HTML><BODY><H1>Hello, world!</H1>"

print "<FORM method='POST'><INPUT name='user'/>"
print "	<INPUT name='password' type='password'>"
print "	<BUTTON type='submit'>Log in</BUTTON>"
print "</FORM>"

print "<P>Query string was: " + os.environ['QUERY_STRING']+"</P>"
print "<P>Your browser is: " + os.environ['HTTP_USER_AGENT']+"</P>"


if loggedinok:
	print "<H2> LOG IN OK! </H2>"


cgi.print_environ()

print json.dumps(dict(os.environ), indent=4)


print "</BODY></HTML>"
