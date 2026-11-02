import cgi
print("Content-type: text/html\n")
form=cgi.FieldStorage()
value=form.getvalue("user_age","default_age")
