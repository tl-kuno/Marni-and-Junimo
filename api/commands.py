from http.server import BaseHTTPRequestHandler
import logging


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers),
                     post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}"
                         .format(self.path).encode('utf-8'))
