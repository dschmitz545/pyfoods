def application(environ, start_response):
    body = b"<h1>Hello World </h1><button>click</button>\n"
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    start_response(status, headers)
    return [body]