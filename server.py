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


import sys, os, BaseHTTPServer

#-------------------------------------------------------------------------------

class ServerException(Exception):
    '''For internal error reporting.'''
    pass

#-------------------------------------------------------------------------------

# __author - Lanre B

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    '''
    If the requested path maps to a file, that file is served.
    If anything goes wrong, an error page is constructed.
    '''
    

    # How to display an error.
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """


    # Classify and handle request
    def do_GET(self):
        try:

            # Figure out what exactly is being requested.
            full_path = os.getcwd() + self.path

            # It doesn't exist...
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))

            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # ...it's something we don't handle.
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))

        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)

    
    # Note that we open the file in binary mode (the b in rb) so that Python wont try to help us by altering byte sequences that look like a Windows line ending.
    # Note also that reading the whole file into memory when serving it is a bad idea in real life, 
    # where the file might be several gigabytes of video data. 
    # Handling that situation is outside the scope of this chapter.

    # read and return content of file requested by user 

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)


    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


    # Handle unknown objects.
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)


#---------------------------------------------------------------------

if __name__ == "__main__":

    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()