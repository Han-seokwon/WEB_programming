#!C:\Users\op\anaconda3\python.exe

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

new_file= open("content/{}.txt".format(title), 'w', encoding='utf-8')
new_file.write(description)

print("Location: index.py?id={}\n".format(title))
