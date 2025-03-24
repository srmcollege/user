class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  
        self.head = 0            
        self.state = 'q0'        

    def move_head(self, direction):
        if direction == 'R':
            self.head += 1
        elif direction == 'L':
            self.head -= 1

    def run(self):
        while self.state != 'halt' and self.state != 'reject':
            current_symbol = self.tape[self.head]

            if self.state == 'q0':  
                if current_symbol == 'a':
                    self.tape[self.head] = 'X'  
                    self.move_head('R')
                    self.state = 'q1'
                else:
                    self.state = 'reject'

            elif self.state == 'q1':  
                if current_symbol == 'b':
                    self.tape[self.head] = 'Y'  
                    self.move_head('R')
                    self.state = 'q2'
                elif current_symbol == 'X':
                    self.move_head('R')  
                else:
                    self.state = 'reject'

            elif self.state == 'q2':  
                if current_symbol == 'c':
                    self.tape[self.head] = 'Z'  
                    self.move_head('L')
                    self.state = 'q3'
                elif current_symbol == 'Y':
                    self.move_head('R')  
                else:
                    self.state = 'reject'

            elif self.state == 'q3':  
                if current_symbol == 'X':
                    self.move_head('L') 
                    self.state = 'q4'
                elif current_symbol == 'Y':
                    self.move_head('L') 
                    self.state = 'q5'
                else:
                    self.state = 'reject'

            elif self.state == 'q4': 
                if current_symbol == 'a':
                    self.tape[self.head] = 'X'  
                    self.move_head('R')
                    self.state = 'q1'
                elif current_symbol == 'Y':
                    self.move_head('R')
                    self.state = 'q5'
                else:
                    self.state = 'reject'

            elif self.state == 'q5':  
                if current_symbol == 'Z':
                    self.move_head('L')
                    self.state = 'q6'
                else:
                    self.state = 'reject'

            elif self.state == 'q6':  
                if self.tape[self.head] == 'X' or self.tape[self.head] == 'Y' or self.tape[self.head] == 'Z':
                    self.move_head('R')
                    self.state = 'halt'  
                else:
                    self.state = 'reject'

        return ''.join(self.tape)

def is_valid_string(input_string):
    """
    Check if the string is of the form a^n b^n c^n.
    """
    n = len(input_string) // 3
    if len(input_string) % 3 != 0: 
        return False
    a_part = input_string[:n]
    b_part = input_string[n:2*n]
    c_part = input_string[2*n:]

    return a_part == 'a' * n and b_part == 'b' * n and c_part == 'c' * n


input_string = input("Enter the string of a's, b's, and c's (in the form a^n b^n c^n): ")

if is_valid_string(input_string):
    tm = TuringMachine(input_string)
    result = tm.run()
    if 'reject' in result:
        print("The string is REJECTED")
    else:
        print("The string is ACCEPTED.")
else:
    print("The string is REJECTED")
