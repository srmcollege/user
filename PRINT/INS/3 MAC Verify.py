import hmac
import hashlib

def generate_mac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

def verify_mac(key, message, mac_to_verify):
    generated_mac = generate_mac(key, message)
    return hmac.compare_digest(generated_mac, mac_to_verify)

key = input("Enter Secret Key: ")
msg = input("Enter the Message : ")

# Generate MAC        
mac = generate_mac(key, msg)
print("\nGenerate MAC(HMAC-SHA256):", mac)

# Verification
recv_mac = input("\nEnter MAC to verify:")

if verify_mac(key, msg, recv_mac):
    print("MAC is valid. Data is authentic and unaltered.")
else:
    print("MAC is invalid. Data may have been tampered.")
