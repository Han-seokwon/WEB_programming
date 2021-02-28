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
    update_link='<a href="update.py?id={}">update</a>'.format(pageID)
    delete_action = '''
        <form action= "process_delete.py" method="get">
            <input type="hidden" name="pageID" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageID)

else:
    pageID = 'WEB'
    description = 'Welcome to my website!'
    update_link=''
    delete_action=''


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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{contents}</p>
</body>
</html>
'''.format(title=pageID, contents=description,
 list_tag=cgiPkg.file_access.get_list(), update_link=update_link,
 delete_action=delete_action))
