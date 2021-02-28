import cgi

print("Content-type: text/plain\n")
form = cgi.FieldStorage()
name = form['name'].value
em = form['email'].value

print('name: ', name)
print('email: ', em)