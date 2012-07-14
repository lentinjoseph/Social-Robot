# TCP server example
import socket
import speech
import eyeapp
import eye
import speakAction
import emotion

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("172.16.50.25", 9900))
server_socket.listen(500)

print "TCPServer Waiting for client on port 9900"
sa=speakAction.sAction()
while(1):
        try:
                
                client_socket, address = server_socket.accept()
                print "I got a connection from ", address
                data=client_socket.recv(28)
                client_socket.close()
                if data.startswith("ILAPPMID"):
                    eye.leftmid()
                    eyeapp.mid()
                    print "EYE LEFT EYE APP MID"
                elif data.startswith("ILAPPDWN"):
                        eye.rightmid()
                        eyeapp.mdown()
                        print "EYE LEFT EYE APP DOWN"
                elif data.startswith("ILAPPUP"):
                        eye.rightmid()
                        eyeapp.up()
                        print "EYE LEFT EYE APP UP"
                elif data.startswith("IRAPPUP"):
                        eye.leftmid()
                        eyeapp.up()
                        print "EYE RIGHT EYE APP UP"
                elif data.startswith("IRAPPMID"):
                        eye.leftmid()
                        eyeapp.mid()
                        print "EYE RIGHT EYE APP MID"
                elif data.startswith("IRAPPDWN"):
                        eye.leftmid()
                        eyeapp.mdown()
                        print "EYE RIGHT EYE APP DOWN"
                elif data.startswith("IMIDAPPUP"):
                        eye.mid()
                        eyeapp.up()
                        print "EYE MID EYE APP UP"
                elif data.startswith("IMIDAPPMID"):
                        eye.mid()
                        eyeapp.mid()
                        print "EYE MID EYE APP DOWN"
                elif data.startswith("IMIDAPPDWN"):
                        eye.mid()
                        eyeapp.mdown()
                        print "EYE MID EYE APP DOWN"
                elif data.startswith("red"):
                        data="i found a red object"
                        no_words=len(data)
                        no_char=0
                        sa.stmt=data
                        sa.speak=True
                        speech.say(data)
                elif data.startswith("blue"):
                        data="i found a blue object"
                        no_words=len(data.split())
                        no_char=0
                        sa.stmt=data
                        sa.speak=True
                        speech.say(data)
                elif data.startswith("love"):
                        emotion.happy()
                
	#while 1:
	#	data = raw_input ( "SEND( TYPE q or Q to Quit):" )
	#	if (data == 'Q' or data == 'q'):
	#		client_socket.send (data)

        #               client_socket.close()
	#		break;
	#	else:
	#		client_socket.send(data)
 
    #           data = client_socket.recv(512)
    #           if ( data == 'q' or data == 'Q'):
	#		client_socket.close()
	#		break;
	#	else:
	#		print "RECIEVED:" , data
	except KeyboardInterrupt:
                server_socket.close()
                exit(0)
