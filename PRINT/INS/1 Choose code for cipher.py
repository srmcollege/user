print("****You Must Need To Select Number Between 1-6****")
print("For Ceaser Cipher Enter number 1")
print("For Monoalphabetic Enter number 2")
print("For RailFence Enter number 3")
print("For Polyaphabetic Enter number 4")
print("For Vernom Cipher Enter number 5")
print("For Verginary Cipher Enter number 6")
while True:
    choice=int(input("Enter A Associated Number To Access The Encryption Techinique:-"))
    if choice==1:
        print("You Select Ceaser Cipher")
        def ceaser_cipherencrypt(plain_text,key):
            result=''
            for a in plain_text:
                if a.isupper():
                    result+=chr(ord(a)+key-65)%26+65
                else:
                    result+=chr((ord(a)+key-97)%26+97)
            return result

        def ceaser_cipherdecrypt(cipher_text,key):
            result=''
            for a in cipher_text:
                if a.isupper():
                    result+=chr(ord(a)-key-65)%26+65
                else:
                    result+=chr((ord(a)-key-97)%26+97)
            return result

        plain_text=input("Enter Your Name: ")
        print(f'Your Text: {plain_text}')
        key=int(input("Enter key: "))
        print(f'Key is: {key}')
        cipher_text=(ceaser_cipherencrypt(plain_text,key))
        print("Encrpted form is:",cipher_text)
        plain_text=(ceaser_cipherdecrypt(cipher_text, key))
        print("Decrpted form is",plain_text)
        
        repeat=input("Do You want to Continue yes/no:-")
        if repeat!="yes":
            print("Good Bye...")
            break
        
        
        
        
    elif(choice==2):
        print("You Select Monoalphabeticr Cipher") 
        def mono_encrypt(cipher):
            plain="abcdefghijklmnopqrstuvwxyz"
            key="zxywvutsrpqomnlkjihgfedcba"
            encrpyted=""
            
            for char in cipher.lower():
                if char in key:
                    index=key.index(char)
                    encrpyted+=plain[index]
                else:
                    encrpyted+=char
            return encrpyted

        def mono_decrypt(cipher):
            plain="abcdefghijklmnopqrstuvwxyz"
            key="zxywvutsrpqomnlkjihgfedcba"
            decrpyted=""
            
            for char in cipher.lower():
                if char in plain:
                    index=key.index(char)
                    decrpyted+=plain[index]
                else:
                    decrpyted+=char
            return decrpyted

        message=input("enter string:")
        cipher=mono_encrypt(message)
        print("encrpyted",cipher)
        dec=mono_decrypt(cipher)
        print("Decrypted",dec)
        
        repeat=input("Do You want to Continue yes/no:-")
        if repeat!="yes":
            print("Good Bye...")
            break
        
        
    elif(choice==3):
        print("You select RailFence Cipher")
        string=input("Enter String: ")
        def RailFence(txt):
            result=""
            for i in range(len(string)):
                if(i%2==0):
                    result+=string[i]
            for i in range(len(string)):
                if(i%2!=0):
                    result+=string[i]
            return result
        print(RailFence(string))
        
        repeat=input("Do You want to Continue yes/no:-")
        if repeat!="yes":
            print("Good Bye...")
            break
        
        
        
        
    elif(choice==4):
        print("You Select Polyalphabetic Cipher")
        def multiplicative_cipher(text,key):
            encrypted=''
            decrypted=''
            
            for char in text:
                if char.isalpha():
                    num=ord(char.upper())-65
                    enc=(num*key)%26
                    encrypted+=chr(enc+65)
                else:
                    encrypted+=char
            try:
                inv_key=pow(key,-1,26)
            except ValueError:
                return "Invalid Key"
            
            for char in encrypted:
                if char.isalpha():
                    num=ord(char.upper())-65
                    dec=(num*inv_key)%26
                    decrypted+=chr(dec + 65)
                else:
                    decrypted+=char
                    
            print("Encrypted: ",encrypted)
            print("Decrypted: ",decrypted)
        multiplicative_cipher("HARSH", 5)
        
        repeat=input("Do You want to Continue yes/no:-")
        if repeat!="yes":
            print("Good Bye...")
            break
        
        
        
        
    elif(choice==5):
        print("You Select Vernom Cipher")
        import random
        import base64

        def generate_key(length):
            return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=length))
        def encrypted(text,key):
            result=''
            for t,k in zip(text,key):
                result+=chr(ord(t)^ord(k))
            return base64.b64encode(result.encode()).decode()
        def decrypted(ciphertext,key):
            decoded=base64.b64decode(ciphertext).decode()
            result=''
            for c,k in zip(decoded,key):
                result+=chr(ord(c)^ord(k))
            return result

        plaintext=input("Enter a Text:-")
        key=generate_key(len(plaintext))

        print("plaintext",plaintext)
        print("key",key)

        ciphertext=encrypted(plaintext, key)
        print("Ciphertext: ",ciphertext)

        decrypted_text=decrypted(ciphertext, key)
        print("Decrypted text:",decrypted_text)
        
        repeat=input("Do You want to Continue yes/no:-")
        if repeat!="yes":
            print("Good Bye...")
            break
  
        
    elif(choice==6):
        print("You Select verginary Cipher")
        def encrypted(text,key):
            encrypted=""
            for i in range(len(text)):
                char=text[i]
                if char.isalpha():
                    shift=ord(key[i%len(key)].lower())-97
                    base=ord('a')
                    encrypted+=chr((ord(char.lower())-base+shift)%26+base)
                else:
                    encrypted+=char
            return encrypted
        
        def decrypted(cihertext,key):
            decrypted=''
            for i in range(len(cihertext)):
                char=cihertext[i]
                if char.isalpha():
                    shift=ord(key[i%len(key)].lower())-97
                    base=ord('a')
                    decrypted+=chr((ord(char.lower())-base-shift)%26+base)
                else:
                    decrypted+=char
            return decrypted
        
        plaintext=input("Enter a text:-")
        key="key"
        ciphertext=encrypted(plaintext, key)
        print("Encrypted text:-",ciphertext)
        decryption=decrypted(ciphertext, key)
        print("Decrypted Text",decryption)
        
        repeat=input("Do You want to Continue yes/no:-")
        if repeat!="yes":
            print("Good Bye...")
            break
    else:
        print("You Select Wrong Number You Must Need To Select Number Between 1-6")

        
    
    
    
