from http.server import HTTPServer
import http_handler
from threading import Thread

class Server():
    #addr - tuple of IP and port
    def __init__(self, addr):
        self.addr = addr
        self.server = HTTPServer(addr, http_handler.webServerHandler)
        self.server_thread = Thread(target = self.server.serve_forever)


    #run httpserver on it's own thread and listen for commands on the main thread
    def run(self):
        self.server_thread.start()
        print("Server started on" + str(self.addr[0]) + ":" + str(self.addr[1]))
        while True:
            command = input("Server:")     
            if command == "shutdown":
                self.server.shutdown()
                self.server_thread.join()
                break





s = Server(("127.0.0.1", 8888))
s.run()
