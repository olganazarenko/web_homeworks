from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib import parse
import os
import mimetypes
from datetime import datetime
import json

templates_path = 'templates'
static_path = 'static'
data_: dict = {}


class CustomTTPRequestHandler(BaseHTTPRequestHandler):
    def send_html_file(self, filename: str, status: int = 200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(os.path.join(templates_path, filename), 'rb') as fd:
            self.wfile.write(fd.read())

   
    def do_GET(self) -> None:
        pr_url = parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        elif Path(static_path, pr_url.path[1:]).exists():
            self.send_static()
        else:
            self.send_html_file('error.html', 404)

    def send_static(self) -> None:
        self.send_response(200)
        types = mimetypes.guess_type(self.path)
        if types:
            self.send_header('Content-type', types[0])
        else:
            self.send_header('Content-type', 'text/plain')

        self.end_headers()
        with open(os.path.join(static_path, self.path[1:]), 'rb') as file:
            self.wfile.write(file.read())

    def do_POST(self) -> None:
        data: bites = self.rfile.read(int(self.headers['Content-Length']))
        print(f'{data=}')
        data_parse = parse.unquote_plus(data.decode())
        print(f'{data_parse=}')
        dict_file: dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        print(f'{dict_file=}')
        data_[str(datetime.now())] = dict_file
        print(f'{data_=}')
        with open('storage/data.json', 'a') as outfile:
            json.dump(data_, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()


def run_server() -> None:
    http = HTTPServer(('127.0.0.1', 3000), CustomTTPRequestHandler)
    try:
        print('In the process...')
        http.serve_forever()
    except KeyboardInterrupt:
        print('\n The server is closed')
        http.server_close()

#
# if __name__ == "__main__":
#     run_server()
