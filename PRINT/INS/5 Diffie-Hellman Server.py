# Diffie-Hellman Key Exchange - Server Side
import socket
import struct
p = 23
g = 5
private_key_server = 6
public_key_server = pow(g, private_key_server, p)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)
print("Server is listening...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

#Send server's public key first
conn.sendall(struct.pack('!I', public_key_server))

#Then receive client's public key
data = conn.recv(4)
if not data:
    print("Client disconnected before sending public key.")
    conn.close()
    server_socket.close()
    exit()
public_key_client = struct.unpack('!I', data)[0]
shared_secret_server = pow(public_key_client, private_key_server, p)
print(f"Server's public key: {public_key_server}")
print(f"Client's public key: {public_key_client}")
print(f"Server's shared secret key: {shared_secret_server}")

# Receive message from client
message = conn.recv(1024).decode()
print(f"Message from client: {message}")

# Optional: Send response
conn.sendall("Message received!".encode())
conn.close()
server_socket.close()
