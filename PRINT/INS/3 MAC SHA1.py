#Importing the hashlib module to use cryptographic hash fumctions
import hashlib

#taking a message input fron the user
inp = input("Enter Message : ")
print("\nOutputing input string into bytes and hashing them using sha1")

#Encoding the input string into bytes and hashing it using SHA1
#inp is encoded to bytes before being hashed
a = hashlib.sha1(inp.encode())
print("\nOutputing the results in hexadecimal format : ")

#.hexdigest() returns the hash function in hexadecimal format
print("The SHA1 first Message is : ")
print(a.hexdigest())
