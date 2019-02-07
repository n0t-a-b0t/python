# Program toi create Simple HTTP/HTTPS server on your local system
# Source: https://gist.github.com/dergachev/7028596
# Original source: http://www.piware.de/2011/01/creating-an-https-server-in-python/
# Generate server.xml with the following command: [NOTE: You need Openssl installed on your system]
#    openssl req -new -x509 -keyout serverkey.pem -out serverkey.pem -days 365 -nodes
# You can visit the server in your browser using:
#    https://localhost:PORT ... for HTTPS, else http://localhost:PORT ... for HTTP

# We import BaseHTTPServer, SimpleHTTPServer and ssl modules.
# If you are just creating HTTP Server, you do not need ssl module
import BaseHTTPServer
import SimpleHTTPServer
import ssl

# We use http daemon (httpd) and create HTTP Server with the HTTPServer class of BaseHTTPServer module and then
# handle requests with the help of SimpleHTTPRequestHandler class of SimpleHTTPServer module
httpd = BaseHTTPServer.HTTPServer(('192.168.254.144', 4448), SimpleHTTPServer.SimpleHTTPRequestHandler)

# We now enable ssl with the openssl certificate created with the above command
# You do not need this line if you are hosting HTTP server
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)

# We host the server for indefinite amount of time with serve_forever() method
httpd.serve_forever()
