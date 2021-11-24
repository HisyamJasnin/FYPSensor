from http.server import HTTPServer,BaseHTTPRequestHandler
import os

def main():
    PORT = 8080
    server = HTTPServer(('', PORT), requestHandler)
    print("Server running on port " + PORT)
    server.serve_forever()
    