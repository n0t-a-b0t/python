# Program to create simple UDP Client in Python
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

# We are going to create an endless loop
while True:
    # We will create a variable to hold our message and then send it to the server over the line
    message = raw_input("Enter your message: ")
    s.sendto(message, (host, port))  # sendto() attribute takes only two values: message and address:port valuse
    # Thus we need to bundle the address:port value together using parenthesis
    # The recvfrom() attribute is used to get the message and address:port value from the Server
    c, adr = s.recvfrom(1024)
    print "Message from: ", adr  # We print the address:port value of the Server
    print "Message Received: ", c  # We print the message from the Server
    # If there is no message from the Server, we break
    if not c:
        break
# We now close the socket and end the connection
s.close()
