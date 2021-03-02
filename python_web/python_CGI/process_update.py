#!C:\Users\op\anaconda3\python.exe

import cgi
import os
import cgitb
cgitb.enable()


form = cgi.FieldStorage()
pageID = form['pageID'].value
title = form['title'].value
description = form['description'].value

new_file= open("content/{}.txt".format(pageID), 'w', encoding='utf-8')
new_file.write(description)
new_file.close()

os.rename("content/{}.txt".format(pageID),'content/{}.txt'.format(title))

print("Location: index.py?id={}\n".format(title))
