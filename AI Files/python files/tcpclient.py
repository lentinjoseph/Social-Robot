# TCP server example
import socket
import bottom
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("172.16.50.25", 9900))
server_socket.listen(5)

print "TCPServe Waiting for client on port 9900"

client_socket, address = server_socket.accept()
print "I got a connection from ", address
bottom.mid()
while(1):

        try:
                
                
                data=client_socket.recv(1)
                if(data=="3"):
                    bottom.mright3()
                elif(data=="4"):
                    bottom.mright2()
                elif(data=="5"):
                    bottom.mright1()
                elif(data=="6"):
                    bottom.mid()
                elif(data=="7"):
                    bottom.mleft5()
                elif(data=="8"):
                    bottom.mleft4()
                elif(data=="9"): 
                    bottom.mleft3()
                print data
        except KeyboardInterrupt:
                client_socket.close()
                server_socket.close()
                exit(0)
	#while 1:
	#	data = raw_input ( "SEND( TYPE q or Q to Quit):" )
	#	if (data == 'Q' or data == 'q'):
	#		client_socket.send (data)
	#		client_socket.close()
	#		break;
	#	else:
	#		client_socket.send(data)
 
    #           data = client_socket.recv(512)
    #           if ( data == 'q' or data == 'Q'):
	#		client_socket.close()
	#		break;
	#	else:
	#		print "RECIEVED:" , data
	
