# Program to create a simple TCP Server in Python
# We will import sys module to demonstrate command line argument operations
# This Program will take in two command line arguments: Server IP and Server Port
# We will also put another argument provision stating the number of messages to transmit
# We will also import socket module for socket operations
import sys
import socket

# Now, we will define variables to store IP and Port number entered as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
# messagelimit = int(sys.argv[3])
# messagelimit += 1  # Here, the limit has to be increased by one to compensate for the while loop operation

# Let's define a variable to hold the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.socket is a constructor
# Now, we will bind host and port together
# s.bind() takes in only one argument, hence we need to bundle host and port together using parenthesis
s.bind((host, port))
# Now, we will let the server listen for any connections
# We can set the number to any connections depending on the system, default value is 1
s.listen(1)
# We create an object 'c' to govern the established connection
# We will use variable adr to store the IP and Port of the Client returned by s.accept()
c, adr = s.accept()
print "Address is: ", adr  # Print the Client IP and Port
# while messagelimit:
while True:  # Creating an infinite loop
    msg = c.recv(1024)  # We set the buffer size to 1024 Bytes
    # If there is no message received yet, break
    if not msg:
        break
    # We Print the received message
    print "Message recieved: %s" % msg
    # We now create a variable to hold our message and then send it over the line
    fox = raw_input("Enter your message: ")
    c.send(fox)
    # messagelimit -= 1
# Finally, we close the connection
c.close()
