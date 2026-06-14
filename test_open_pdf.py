import http.server
import socketserver
import webbrowser
import threading
import os
import time

PORT = 8000
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
PDF_NAME = "matlab_onramp_certificate.pdf"

os.chdir(ASSETS_DIR)
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

def serve():
    with httpd:
        httpd.serve_forever()

thread = threading.Thread(target=serve, daemon=True)
thread.start()

url = f"http://localhost:{PORT}/{PDF_NAME}"
print(f"Serving {ASSETS_DIR} on port {PORT}")
print(f"Opening {url} in your default browser...")
webbrowser.open(url)

# keep server alive briefly so the browser can fetch the file
try:
    time.sleep(15)
finally:
    httpd.shutdown()
    print("Server stopped")
