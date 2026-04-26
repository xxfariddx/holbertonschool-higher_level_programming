from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):

    # -----------------------------
    # Handle GET requests
    # -----------------------------
    def do_GET(self):

        # Root endpoint "/"
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpoint
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())

        # /status endpoint
        elif self.path == "/status":
            data = {"status": "OK"}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())

        # Undefined routes → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode())


# -----------------------------
# Start server
# -----------------------------
def run():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPI)

    print("Server running on http://localhost:8000")
    httpd.serve_forever()


# Run the server
if __name__ == "__main__":
    run()
