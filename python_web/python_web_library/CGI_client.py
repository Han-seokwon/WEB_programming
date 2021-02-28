from urllib.request import urlopen
from urllib.parse import urlencode

url ='http://192.168.0.10:9999/cgi-bin/script.py'

data = {
    'name' : 'Han seokwon',
    'email' : 'hanseokwon@han.com'
}

Enc_data = urlencode(data)

#POST 요청
a = urlopen(url, Enc_data.encode('ascii'))
print(a.read().decode('cp949'))