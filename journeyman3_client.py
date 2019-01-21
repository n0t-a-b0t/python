import socket

host = '127.0.0.1'
port = 50004

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("Hello")

while True:
    c = s.recv(1024)
    if not c:
        break
    else:
        print "Message from server: ", c
s.close()
