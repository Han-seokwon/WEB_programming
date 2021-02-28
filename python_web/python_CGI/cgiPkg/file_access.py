import os, html_sanitizer


def get_list():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('content')
    list_str=''
    for i in files:
        i = sanitizer.sanitize(i)
        list_str += '<li><a href="index.py?id={index_name}">{index_name}</a></li>'.format(index_name=i[:-4])
    return list_str
