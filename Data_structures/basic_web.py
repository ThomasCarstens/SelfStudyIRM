import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

#Create a MyHandler class which extends
#http.server.SimpleHTTPRequestHandleroverride
#the do_GET method to print something in the console,
#then call the superdo_GET method

#Make the server stop on the third page load
