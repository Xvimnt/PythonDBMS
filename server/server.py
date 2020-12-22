# Imports
import io
import os
import json
# Librerias para el servidor
import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
            self.send_response(200)
            self.wfile.write(bytes("Ok",'utf-8'))

TytusServer = HTTPServer(('localhost', 4040), Handler)
print("Corriendo server en puerto 4040")
TytusServer.serve_forever()