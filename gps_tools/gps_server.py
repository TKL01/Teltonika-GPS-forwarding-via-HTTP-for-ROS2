from http.server import BaseHTTPRequestHandler, HTTPServer

class GPSHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Output of received data 
        print(f"Headers: {self.headers}")
        print(f"Body: {post_data}")

        try:
            # temporarly store NMEA data in a file
            with open('/tmp/gps_data.nmea', 'w') as file:
                file.write(post_data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        except Exception as e:
            print(f"Error: {e}")
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Bad Request')

def run(server_class=HTTPServer, handler_class=GPSHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}')
    httpd.serve_forever()

def main():
    run()

if __name__ == "__main__":
    main()



