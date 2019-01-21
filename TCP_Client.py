# Program to create simple TCP Client in Python
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

# Let's define a variable to hold the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Now, we will connect the server on the mentioned IP and Port
# s.connect() takes only one argument, hence we need to bundle IP and Port together by using parenthesis
s.connect((host, port))
# We will now send a message to the server that the connection is established
messg = "Connection Established"
s.send(messg)
# while messagelimit:
# We will now create an infinite loop for communications
while True:
    # We set the receiving buffer to 1024 Bytes
    messg1 = s.recv(1024)
    # If we did not receive any message from the server, we break
    if not messg1:
        break
    # We will print the received message
    print messg1
    # Now, we will create a variable to hold our own messages and send it over the line
    fox = raw_input("Enter your message: ")
    s.send(fox)
    # messagelimit -= 1
# We will now close the connection
s.close()
