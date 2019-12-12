#Basic HTTP server
#reacts to GET and POST requests only
#launches on localhost:9999, you can change params if you want
from http.server import BaseHTTPRequestHandler, HTTPServer 
import threading
import re
import os.path
import json
from ml_service import MLService


#Handling strategy for this WebServer
class webServerHandler(BaseHTTPRequestHandler):

    #initializes this web server
    #site_path - path to index.html file
    def __init__(self, request, client_address, server):
        self.site = "<html><body><h1>Error loading page</h1></body></html>"
        self.root = "../site/"
        with open("../site/index.html") as f:
            self.site = f.read()
        super().__init__(request, client_address, server)

    #sets default headers
    def _headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    #method that will be called when user requests something from a server with a GET request
    #sends requested file to a user 
    def do_GET(self):
        #prepare file path
        true_path = self.root
        if self.path == "/":
            true_path += "index.html" #if site root was requested, serve index.html 
            self._headers()
        else:
            true_path += self.path[1:] #because self.path begins with '/' we silce it out

        #check if file even exists and if it is valid
        if os.path.exists(true_path) == False or os.path.isfile(true_path) == False:
            self.send_response(404) #TODO: Investigate why 404 is sent 8 times in a row
            return


        #check what type of file is being requested and send appropiate meta-data
        if re.match("\.js$", self.path):
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()
        elif re.match("\.html$", self.path):
            self._headers()
        #at the end write requested file to the send buffer
        with open(true_path) as f:
            self.wfile.write(bytes(f.read(), 'utf-8'))

    #method that will be called when user wants to write some data to a server with a POST request
    #gets image data from a user and redirects it to a ML service
    #then sends JSON data about what ML service thinks that user has written
    def do_POST(self):
        self.send_response(200);
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length)
        json_data = json.loads(data.decode("utf-8"))
        #pass json_data to ML service
        ml = MLService()
        ml.evaluate(json_data)







