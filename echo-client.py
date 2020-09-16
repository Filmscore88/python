import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("whois.godaddy.com", 43))

    s.sendall(b'Hello, world')
    data = s.recv(1024)

    print("Expiration Date: ", s.expiration_date)
