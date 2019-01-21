import socket

host = '127.0.0.1'
port = 20025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("Hello")
while True:
    mess1 = s.recv(1024)
    s.send("Moving on...")
    mess2 = s.recv(1024)
    print mess2
    if mess2 == 'Enter choice: 1 - write to a file | 2 - View a file: ':
        mess3 = int(raw_input("Enter the choice: "))
        if mess3 == 1 or mess3 == 2:
            s.send(str(mess3))
            mess4 = s.recv(1024)
            print mess4
            if mess4 == 'Writing to a file....':
                mess5 = raw_input("Enter the filename: ")
                s.send(mess5)
                mess6 = s.recv(1024)
                print mess6
                mess7 = raw_input()
                s.send(mess7)
                mess8 = s.recv(1024)
                print mess8
                break
            if mess4 == 'Reading from file....':
                mess5 = raw_input("Enter filename: ")
                s.send(mess5)
                mess6 = s.recv(1024)
                print mess6
                break
        else:
            print "Enter either 1 or 2"
            break
s.close()
