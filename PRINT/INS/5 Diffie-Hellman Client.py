# Diffie-Hellman Key Exchange - client Side
import socket
import struct
p = 23
g = 5
private_key_client = 3
public_key_client = pow(g, private_key_client, p)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

#receive server's public key
data = client_socket.recv(4)
public_key_server = struct.unpack('!I', data)[0]

#send client's public key
client_socket.sendall(struct.pack('!I', public_key_client))
shared_secret_client = pow(public_key_server, private_key_client, p)
print(f"Client's public key: {public_key_client}")
print(f"Server's public key: {public_key_server}")
print(f"Client's shared secret key: {shared_secret_client}")

# Send message
message = input("Enter message to send to server: ")
client_socket.sendall(message.encode())

# Receive response
response = client_socket.recv(1024).decode()
print(f"Response from server: {response}")
client_socket.close()
