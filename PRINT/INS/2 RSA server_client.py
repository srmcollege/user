import math

def gcd(a, h):
    while h != 0:
        a, h = h, a % h
    return a

# Extended Euclidean Algorithm to find multiplicative inverse
def multiplicative_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Input two prime numbers
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

# Compute n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that e and phi(n) are coprime
e = 3
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 2  # Increment by 2 to keep e odd

# Compute d (modular inverse of e mod phi)
d = multiplicative_inverse(e, phi)
if d is None:
    print("Failed to find modular inverse. Try different primes.")
    exit()

# Message to encrypt
pt = int(input(f"Enter a plain text number (less than {n}): "))
if pt >= n:
    print("Plaintext must be less than n.")
    exit()

print("Message data:", pt)

# Encryption
c = pow(pt, e, n)
print("Encrypted Data:", c)

# Decryption
m = pow(c, d, n)
print("Decrypted Data:", m)
