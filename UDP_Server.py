# Program to create simple UDP Server in Python
# We will import sys module for command line argument operations
# We will take in two command line arguments: Server IP and Port Number
# We will import socket module for socket operations
import sys
import socket

# We now create variables to hold our command line arguments
host = sys.argv[1]
port = int(sys.argv[2])

# We now create an object variable for the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# We will bind the socket to the specified port
# s.bind takes in only one argument, hence we need to bundle IP and Port number together using parenthesis
s.bind((host, port))

# We are going to create an endless loop
while True:
    # We use recvfrom() attribute to separate the received message and the client address:port values
    c, adr = s.recvfrom(1024)
    print "Connection Established from: ", adr  # We print out the Client's address:port value
    print "Message Received: ", c  # We print out the received message
    # If there is now message received, we break
    if not c:
        break
    # We now create a variable to hold our own message and send it to the client over the line
    messg = raw_input("Enter your message: ")
    s.sendto(messg, adr)
# We now close the connection
s.close()
