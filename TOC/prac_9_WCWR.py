2
def is_valid_wcwr(string):
    stack=[] 
    found_c=False
    
    for char in string: 
        if char=='c':
            if not stack:
                return False
            found_c=True
        elif not found_c:
            stack.append(char)
        else:
            if not stack[-1]!=char:
                return False
            stack.pop()
            
    return found_c and not stack
    
binary_string=input("Enter a string in WCWR format:-") 
if is_valid_wcwr (binary_string):
    print("String Is Acceped It Follow WCWR pattern")
else:
    print("String Is Rejected It doesn't Follow WCWR pattern")