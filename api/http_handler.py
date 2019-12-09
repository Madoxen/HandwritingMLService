#Basic HTTP server
#reacts to GET and POST requests only
#launches on localhost:9999, you can change params if you want
from http.server import BaseHTTPRequestHandler, HTTPServer 
import threading


#Handling strategy for this WebServer
class webServerHandler(BaseHTTPRequestHandler):

    #initializes this web server
    #site_path - path to index.html file
    def __init__(self, request, client_address, server):
        self.site = "<html><body><h1>Error loading page</h1></body></html>"
        super().__init__(request, client_address, server)
        with open("../site/index.html") as f:
            self.site = f.readlines()

    #sets default headers
    def _headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    #reaction to user sending GET request to a server
    #sends index.html to a user
    def do_GET(self):
        #send site
        self._headers()
        self.wfile.write(bytes(self.site, 'utf-8'))

    #reaction to user sending POST request to a server
    #gets image data from a user and redirects it to a ML service
    #then sends JSON data about what ML service thinks that user has written
    def do_POST(self):
        self._headers()
        self.wfile.write("<html><body><b>POSTED</b></body></html>")



