import random
import base64
def generate_key(length):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))
def encrypt(text, key):
    result = ''
    for t, k in zip(text, key):
        result += chr(ord(t) ^ ord(k))
    return base64.b64encode(result.encode()).decode()
def decrypt(ciphertext, key):
    decoded = base64.b64decode(ciphertext).decode()
    result = ''
    for c, k in zip(decoded, key):
        result += chr(ord(c) ^ ord(k))
    return result
# Execution starts here:-
plaintext = "HELLO"
key = generate_key(len(plaintext))
print("plaintext:", plaintext)
print("Key:", key)
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("decryptedtext:", decrypted_text)
