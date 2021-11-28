from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import tempsensor
import waterlevel

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response_only(200)
            self.end_headers()
            tempsensor.main_temp()
            waterlevel.main_water()
        elif self.path == "/run":
            print("Running sprinkler")

def main():
    PORT = 9001
    server = HTTPServer(('', PORT), requestHandler)
    print("Server running on port " + str(PORT))
    server.serve_forever()
    
if __name__ == '__main__':
    main()
    
   
