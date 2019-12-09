from http.server import HTTPServer
import http_handler
from threading import Thread

class Server():
    #addr - tuple of IP and port
    def __init__(self, addr):
        self.addr = addr
        self.server = HTTPServer(addr, http_handler.webServerHandler)
        self.server_thread = Thread(target = self.server_loop)
        self.restarting = False

    #run httpserver on it's own thread and listen for commands on the main thread
    def run(self):
        self.server_thread.start()
        print("Server started on" + str(self.addr[0]) + ":" + str(self.addr[1]))
        while True:
            command = input("comm:")     
            if command == "shutdown":
                self.server.shutdown()
                print("Server shutting down...")
                self.server_thread.join() #wait for thread to safely terminate
                break
            elif command == "restart":
                self.restarting = True
                self.server.shutdown()
                print("Server restarting...")


    #operates server running and it's interrupts
    def server_loop(self):
        print("Server instance running")
        while True:
            self.server.serve_forever()
            if self.restarting == False:
                break
            else:
                self.restarting = False #After restart, set the restart flag to False again


s = Server(("127.0.0.1", 8888))
s.run()
