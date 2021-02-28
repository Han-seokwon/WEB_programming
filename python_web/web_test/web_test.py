from wsgiref.simple_server import make_server

def app1(environ, start_response):
    
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    
    response =['Hello WSGI'.encode('utf-8')] # iterable

    return response

print("Serving HTTP on port 8000...")
server = make_server('', 8000, app1)
server.serve_forever()