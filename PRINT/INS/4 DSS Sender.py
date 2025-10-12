#run this command on cmd first - pip install pycryptodome

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

#input message from sender
message = input("Sender:Enter your messages:")

with open('message.txt','w')as f:
    f.write(message)

#Generate RSA key pair
random_generator = Random.new().read
key_pair = RSA.generate(2048,random_generator)

#Extract public and private keys
public_key = key_pair.publickey().export_key()
private_key = key_pair.export_key()

#Display public key for reference
print("sender:public key:\n",public_key.decode())

def generate_signature(private_key,message):
    key=RSA.import_key(private_key)
    hashed_message=SHA256.new(message.encode('utf-8'))
    signer=PKCS1_v1_5.new(key)
    signature=signer.sign(hashed_message)
    return signature

#generate digital signature
signature = generate_signature(private_key,message)

#save public key, private key, message, and signature to files

with open('public_key.txt','wb')as f:
    f.write(public_key)

with open('private_key.txt','wb')as f:
    f.write(private_key)

with open('signature.sig','wb')as f:
    f.write(signature)

print("\nSender: All data saved successfully.")
print("Sender: Message sent:",message)
print("Sender: Digital signature generated and saved.")


