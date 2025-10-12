import socket
import math

# Prime number check
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True  # Fixed indentation

def compute_n(p, q):
    return p * q

def compute_quotient(p, q):
    return (p - 1) * (q - 1)

def find_public_key(quotient):
    e = 2
    while e < quotient:
        if math.gcd(e, quotient) == 1:
            return e
        e += 1
    raise Exception("No valid public key found")

def find_private_key(e, quotient):
    d = 1
    while (d * e) % quotient != 1:
        d += 1
    return d  # Fixed: was returning early

def decrypt(cipher_text, d, n):
    return pow(cipher_text, d, n)

# Create and bind server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen()  # Fixed: was missing newline or semicolon
print("Server listening on port 65432...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Step 1: Receive p and q
p_q_data = conn.recv(1024).decode()
p_str, q_str = p_q_data.strip().split()
p, q = int(p_str), int(q_str)  

# Step 2: Calculate RSA keys
n = compute_n(p, q)
quotient = compute_quotient(p, q)
e = find_public_key(quotient)
d = find_private_key(e, quotient)

# Send RSA keys to client
key_info = f"{n} {e} {d}"  
conn.sendall(key_info.encode())
print(f"Sent RSA keys (n={n}, e={e}, d={d}) to client")

# Step 3: Receive cipher-text
ciphertext_data = conn.recv(1024).decode()
ct_blocks = list(map(int, ciphertext_data.strip().split()))
print(f"Received encrypted blocks: {ct_blocks}")

# Step 4: Decrypt cipher-text
pt_blocks = [decrypt(c, d, n) for c in ct_blocks]
print(f"Decrypted numeric blocks: {pt_blocks}")

# Step 5: Convert numeric blocks to text
decrypted_text = ''.join(chr(pt + 97) for pt in pt_blocks)
print(f"Decrypted text: {decrypted_text}")

# Send decrypted text back to client
conn.sendall(decrypted_text.encode())

# Close connection
conn.close()
print("Connection closed")


