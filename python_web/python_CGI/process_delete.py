#!C:\Users\op\anaconda3\python.exe

import cgi
import cgitb
import os
cgitb.enable()

form = cgi.FieldStorage()
pageID = form['pageID'].value

os.remove("content/{}.txt".format(pageID))

print("Location: index.py\n")
