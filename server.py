"""
Hello, Web. 

The basic idea is simple:

- Wait for someone to connect to our server and send an HTTP request; 
- parse that request;
- figure out what it's asking for;
- fetch that data (or generate it dynamically);
- format the data as HTML; and
- send it back.
"""


import BaseHTTPServer 

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    # Handle HTTP requests by returning a fixed 'page '

        # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''


# Get requests 
def do_GET(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.send_header("Content-Length", str(len(self.Page)))
    self.end_headers()
    self.wfile.write(self.Page)




#----------------------------------------------------------------------


if __name__ == "__main__":
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()