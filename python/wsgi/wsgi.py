# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


def hello_world_app(environ, start_response):
    """每个 WSGI 应用程序都应该有一个 Application 对象，一个接受
    evirion 和 start_response 参数的 callable(可调用）对象
    """
    status = "200 OK"
    headers = [('Content-Type', 'text/plain; chartset=utf-8')]
    start_response(status, headers)
    return [b'Hello, World']


httpd = make_server('', 8000, hello_world_app)
print('Serving on port 8000 ...')
# 服务直到进程被 killed 
httpd.serve_forever()
