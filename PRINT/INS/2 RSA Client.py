import socket

# RSA Encryption function
def encrypt(plain_text, e, n):
    return pow(plain_text, e, n)

# Prime check function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True  

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client_socket.connect(('localhost', 65432))  

# Step 1: Input prime numbers p and q
print('\nStep 1: Get Prime numbers')
while True:
    try:
        p = int(input("Enter a prime number for p: "))
        q = int(input("Enter a prime number for q: "))  
        if is_prime(p) and is_prime(q):
            break
        else:
            print("Both numbers must be prime. Try again.")
    except ValueError:
        print("Invalid input. Please enter integers.")

# Send p and q to the server
client_socket.sendall(f'{p} {q}'.encode()) 

# Step 2: Receive RSA keys (n, e, d)
print("\nStep 2: Receive keys from server")
response = client_socket.recv(1024).decode()
n, e, d = map(int, response.split())

# Step 3: Input plaintext
while True:
    alphabetic_text = input("Enter plain text (letters only): ").strip().lower()
    if alphabetic_text.isalpha():
        break
    else:
        print("Please enter letters only.")

# Convert plaintext to numeric (a=0, b=1, ..., z=25)
pt_blocks = [ord(char) - 97 for char in alphabetic_text]
print(f"Numeric blocks: {pt_blocks}")

# Step 4: Encrypt numeric blocks
print("\nStep 4: Encrypt plain-text")
ct_blocks = [encrypt(pt, e, n) for pt in pt_blocks]
print(f"Encrypted ciphertext blocks: {ct_blocks}")

# Send ciphertext to server
client_socket.sendall(" ".join(map(str, ct_blocks)).encode())

# Step 5: Receive decrypted text from server
print("\nStep 5: Receive decrypted text")
decrypted_text = client_socket.recv(1024).decode()
print(f"Decrypted text from server: {decrypted_text}")

# Close connection
client_socket.close()
