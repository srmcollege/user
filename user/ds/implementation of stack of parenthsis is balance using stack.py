def stack(s):
    parentheses = {')': '(', ']': '['}
    
    stack = []
    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if not stack or stack[-1] != parentheses[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

strings = [
    "()",        
    "([])",    
    "([)]",   
    "((()))",    
    "(()",     
    "([)]"     
]

for s in strings:
    result = stack(s)
    print(f"'{s}' is balanced: {result}")
