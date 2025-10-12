def caesar_cipher_encrypt(plain_text, key):
    result = ''
    for i in plain_text:
        if i.isupper():
            result += chr((ord(i) + key - 65) % 26 + 65)
        else:
            result += chr((ord(i) + key - 97) % 26 + 97)
    return result
def caesar_cipher_decrypt(cipher_text, key):
    result = ''
    for i in cipher_text:
        if i.isupper():
            result += chr((ord(i) - key - 65) % 26 + 65)
        else:
            result += chr((ord(i) - key - 97) % 26 + 97)
    return result
plain_text = input('Enter plain text: ')
print(f'String is: {plain_text}')
key = int(input('Enter key: '))
print(f'Key is: {key}')
cipher_text = caesar_cipher_encrypt(plain_text, key)
print(cipher_text)
print(caesar_cipher_decrypt(cipher_text, key))
