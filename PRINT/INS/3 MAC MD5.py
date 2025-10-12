import hashlib

msg1 = input("Enter Message 1 : ")
msg2 = input("Enter Message 2 : ")

print("\nEncoding the input strings into bytes and hashing them using MD5")

# Encoding the input
data1 = hashlib.md5(msg1.encode())#inp1 is encoded to byte and hashed
data2 = hashlib.md5(msg2.encode())

print("\nOutputing the results in byte format")

print("The MD5 hash of the first message is : ")
print(data1.digest())#returns the MD5 hash in bytes

print("The MD5 hash of the second message is : ")
print(data2.digest())


