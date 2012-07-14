import socket
import threading
import os


class redDetect(threading.Thread):

    server_socket=None
    client_socket=None
    data=None
    def __init__(self):
        data=None
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("172.16.50.25", 9500))
        server_socket.listen(5)
        threading.Thread.__init__(self,None)
        self.start()

    def run(self):
        while(1):
            client_socket, address = server_socket.accept()
            print "I got a connection from ", address
            data=client_socket.recv(33)
            client_socket.close()
            os.system("sleep 1")
            data=None
            
