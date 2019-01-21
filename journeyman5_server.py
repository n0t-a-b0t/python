import socket

host = ''
port = 20025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def listening():
    s.listen(1)
    c, addr = s.accept()
    mess1 = c.recv(1024)
    print mess1
    c.send(mess1)
    while True:
        try:
            mess = c.recv(1024)
            c.send("Enter choice: 1 - write to a file | 2 - View a file: ")
            mess2 = c.recv(1024)
        except:
            print "Some Error occurred... Restarting"
            listening()
        else:
            if mess2 == '1':
                c.send("Writing to a file....")
                mess3 = c.recv(1024)
                fileobj = open(mess3, 'a+')
                c.send("Enter the contents: ")
                mess4 = c.recv(1024)
                fileobj.write(mess4)
                fileobj.close()
                c.send("Contents written....")
            elif mess2 == '2':
                c.send("Reading from file....")
                mess3 = c.recv(1024)
                try:
                    fileobj = open(mess3, 'r')
                except:
                    mess4 = "No such file..."
                    c.send(mess4)
                else:
                    mess4 = fileobj.read(1024)
                    fileobj.close()
                    c.send(mess4)
                finally:
                    c.send("\n\n\n----End of File----")
    c.close()
    s.close()
    return


listening()
