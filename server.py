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

import time 
import BaseHTTPServer 

# __author - Lanre B

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    
    # Handle HTTP requests by returning a fixed 'page '

        # Page to send back.
    Page = '''\
<html>
<body>
<table border=1s>
            <tr> <td>Header</td> <td>Value</td> </tr>
            <tr> <td>Date and time</td> <td> {date_time} </td> </tr>
            <tr> <td>Client host</td> <td>  {client_host} </td> </tr>
            <tr> <td>Client port</td> <td>  {client_port} </td> </tr>
            <tr> <td>Command</td> <td>  {command} </td> </tr>
            <tr> <td>Path</td> <td> {path} </td> </tr>
        </table>
</body>
</html>
'''


# Get requests 

    def do_GET(self):
        page = self.create_page()
        self.send_page(page)


    def create_page(self):

        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path
        } 

        print(values)

        page = self.Page.format(**values)
        return page 

    

    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page) 


#---------------------------------------------------------------------


if __name__ == "__main__":

    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()