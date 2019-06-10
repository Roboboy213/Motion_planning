import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.43.135", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
