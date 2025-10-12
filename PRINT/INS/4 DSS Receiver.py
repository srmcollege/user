from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

#function to verify the signature
def verify_signature(public_key,message,signature):
    key=RSA.import_key(public_key)
    hashed_message=SHA256.new(message.encode('utf-8'))
    verifier=PKCS1_v1_5.new(key)
    return verifier.verify(hashed_message,signature)

#Load public key from file
with open('public_key.txt','rb')as f:
    public_key = f.read()
    print("Receiver: Public Key Loaded:\n",public_key.decode())

#Load Message from file
with open('message.txt','r')as f:
    message = f.read()
    print("Receiver: Message received:\n",message)

#Load signature from file
with open('signature.sig','rb')as f:
    signature = f.read()
    print("Receiver: Signature loaded.")

#verify the digital signature
is_valid = verify_signature(public_key,message,signature)

if is_valid:
    print('''\nReceiver: Signature Verification Result:
       The Signature is valid. Message authenticity confirmed!''')
else:
    print('''\nReceiver: Signature Verification Result:
       The Signature is invalid. Message authenticity cannot be confirmed!''')



