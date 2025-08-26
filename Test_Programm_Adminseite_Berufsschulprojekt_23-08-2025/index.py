import http.server
import socketserver

PORT = 8080  # Render verwendet oft Port 10000, aber 8080 ist Standard

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server läuft auf Port {PORT}")
    httpd.serve_forever()
