import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import io
import os
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
            self.send_response(400)
            self.wfile.write(bytes("",'utf-8'))

myServer = HTTPServer(('localhost', 4040), MyRequestHandler)
print("Corriendo server en puerto 4040")
myServer.serve_forever()