import socket

host = ''
port = 50004

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

c, addr = s.accept()

while True:
    c.recv(1024)
    if not c:
        break
    else:
        print "Connection request from: ", addr
        message = "This message is from the server!"
        c.send(message)
c.close()
s.close()
