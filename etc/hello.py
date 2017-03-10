def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes(environ['QUERY_STRING'].replace('&', '\n'), 'utf-8')]
