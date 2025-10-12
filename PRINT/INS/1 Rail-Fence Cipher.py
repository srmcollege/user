def Railfence(text):
    result = ""
    # First rail: even indices
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i]
    # Second rail: odd indices
    for i in range(len(text)):
        if i % 2 != 0:
            result += text[i]
    return result
# Input from user
text = input("Enter a string: ")
print("Encrypted using Rail Fence (2 rails):", Railfence(text))
