text = "helloworld"
key = "key"
def encrypt(text, key):
    encrypted = ""
    for i in range(len(text)): 
        char = text[i]           
        if char.isalpha():     
            shift = ord(key[i % len(key)].lower()) - 97
            base = ord('a')
            encrypted += chr((ord(char.lower()) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted  # Corrected indentation
def decrypt(text, key):
    decrypted = ""
    for i in range(len(text)): 
        char = text[i]           
        if char.isalpha():     
            shift = ord(key[i % len(key)].lower()) - 97
            base = ord('a')
            decrypted += chr((ord(char.lower()) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted  # Corrected indentation
encrypted_text = encrypt(text, key)
decrypted_text = decrypt(encrypted_text, key)
print("The text is:", text)
print("The key is:", key)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)	
