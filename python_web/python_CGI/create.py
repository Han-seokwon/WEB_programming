#!D:\Bitnami\wampstack-8.0.1-0\apache2\htdocs\python_study\CGI\CGI_env\Scripts\python.exe

print("content-type: text/html;charset='utf-8'\n")
import cgitb
cgitb.enable()

import cgi
import sys
import codecs
import os
import cgiPkg.file_access
import html_sanitizer
sanitizer = html_sanitizer.Sanitizer()


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


form = cgi.FieldStorage()
if 'id' in form:
    pageID = form["id"].value
    pageID = sanitizer.sanitize(pageID)
    description = open("content/"+pageID+'.txt', 'r', encoding="utf-8" ).read()
    description= sanitizer.sanitize(description)
else:
    pageID = 'WEB'
    description = 'Welcome to my website!'

print('pageID: ',pageID)
print('''<!DOCTYPE html>
<html>
<head>
  <title>WEB</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {list_tag}
  </ol>
  <a href="create.py">create</a>
  <form action='process_create.py' method='post' autocomplete='on'>
      <p><input type="text" name='title' placeholder='title'></p>
      <p><textarea rows='15' cols='50' name='description' placeholder='description'></textarea></p>
      <p><input type='submit'></p>
  </form>
  <h2>{title}</h2>
  <p>{contents}</p>
</body>
</html>
'''.format(title=pageID, contents=description,
list_tag=cgiPkg.file_access.get_list()))
