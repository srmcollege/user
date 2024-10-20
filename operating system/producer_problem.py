


number = int(input("Enter the length of buffer: "))
buffer_list = []

while len(buffer_list) < number:
    ask = int(input("Enter 1 to produce, Enter 2 to consume, enter 3 to exit: "))
    
    if ask == 1:
        value = int(input("Enter the item to produce: "))
        buffer_list.append(value)
        print(f"Item {value} added to buffer.")
        
    elif ask == 2:
        if len(buffer_list) > 0:
            value2 = int(input("Which product you want to access (0 to {len(buffer_list)}): "))
            buffer_list.append(value2)
            if value2 < len(buffer_list):
                print(f"Product accessed: {buffer_list[value2]}")
                buffer_list.pop(value2)
            else:
                pass











