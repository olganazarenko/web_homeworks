from http.server import HTTPServer, BaseHTTPRequestHandler
import os

template_path = 'templates/'


class CustomTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        file = 'index.html'
        print(f'{self, path=}')
        self.send_response(200, "Hello. My name is Star")
        self.send_header('content-type', 'text/html')
        self.send_headers()
        with open(template_path, 'rb') as file:
            self.wfile.write(file.read())


def run():
    http = HTTPServer(('localhost', 5000), CustomTTPRequestHandler)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run()
