import hashlib
def hash_choice(message1, message2, choice):
    if choice == 1:
        a = hashlib.md5(message1.encode())
        b = hashlib.md5(message2.encode())
        print("\nOutputting the results in hexadecimal format")
        print("The MD5 hash of the first message is:")
        print(a.hexdigest())
        print("The MD5 hash of the second message is:")
        print(b.hexdigest())
    elif choice == 2:
        a = hashlib.sha1(message1.encode())
        b = hashlib.sha1(message2.encode())
        print("\nOutputting the results in hexadecimal format")
        print("The SHA1 hash of the first message is:")
        print(a.hexdigest())
        print("The SHA1 hash of the second message is:")
        print(b.hexdigest())
    else:
        print("Invalid choice.")
        return
# Step 1: Get messages
message1 = input("Enter first message: ")
message2 = input("Enter second message: ")
# Step 2: First time asking choice
choice = int(input("Choose hash function: 1 for MD5, 2 for SHA1: "))
hash_choice(message1, message2, choice)
# Step 3: Ask again at the end
repeat = input("\nDo you want to try again with another hash function? (yes/no): ").strip().lower()
if repeat == "yes":
    choice2 = int(input("Choose hash function again: 1 for MD5, 2 for SHA1: "))
    hash_choice(message1, message2, choice2)
else:
    print("Thank you!")
