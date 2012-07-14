#!/usr/bin env python
# TCP client example
import socket
file=open("sample.txt")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("172.16.50.25", 9900))
data=file.read()
print data
client_socket.send(data)
client_socket.close()
        
            
