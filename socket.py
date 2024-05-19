#client side
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(b"Hello, world.... sent by client")
data = s.recv(1024)
print(data)
##########################################
#server side
import socket			 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
	 
print ("socket binded to %s" %(PORT)) 
print ("socket is listening....")		 


while True: 

    con, addr = s.accept()	 
    print ('Got connection from', addr )

    con.send(b"Thank you for connecting...sent by server")

    data = con.recv(1024) 
    print(f"Received {data!r}")

    con.close()

    break

###################################################################
# An example script to connect to Google using socket 
import socket  
import sys 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print ("Socket successfully created")

port = 80

try: 
	host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 

	print ("there was an error resolving the host")
	sys.exit() 

s.connect((host_ip, port)) 

print ("the socket has successfully connected to google") 
print (host_ip)
