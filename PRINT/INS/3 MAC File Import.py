### Create file macdata.txt ###

import hashlib
file_path = input("Enter the path of the file: ").strip().strip('"')
def hash_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            # Display actual file content (text)
            print("\nActual file content:")
            try:
                print(data.decode('utf-8'))  # try decoding as UTF-8
            except UnicodeDecodeError:
                print("[Binary or non-text file: cannot display content]")
            # Correct: no .encode()
            a = hashlib.sha1(data)
            print("\nOutputting the results in hexadecimal format")
            print("The SHA1 hash of the file is:")
            print(a.hexdigest())
    except FileNotFoundError:
        print("File not found. Please check the path.")
    except Exception as e:
        print(f"Error: {e}")
hash_file(file_path)


