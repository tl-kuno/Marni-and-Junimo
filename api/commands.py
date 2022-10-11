from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)
        self._set_response()
        self.wfile.write("POST request for {}"
                         .format(self.path).encode('utf-8'))
