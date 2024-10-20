'''
import threading
from time import sleep

def addition(num1, num2):
    num3 = num1 + num2
    print(f"Addition of {num1} and {num2} is :{num3}")
    sleep(0.3)
    
def subtract(num1, num2):
    num3 = num1 - num2
    print(f"Subtraction of {num1} and {num2} is :{num3}")
    sleep(0.2)
    
def multiplication(num1, num2):
    num3 = num1 * num2
    print(f"Multiplication of {num1} and {num2} is: {num3}")
    sleep(0.3)
    
def square(nums):
    for num in nums:
        sleep(0.6)
        print(f"Square of {num} is {num*num}")

def cube(nums):
    for num in nums:
        sleep(0.6)
        print(f"Cube of {num} is {num*num*num}")

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Array for square and cube functions
arr = [4, 7, 3, 21]

# Create threads for each operation
addition_thread = threading.Thread(target=addition, args=(num1, num2))
subtract_thread = threading.Thread(target=subtract, args=(num1, num2))
multiplication_thread = threading.Thread(target=multiplication, args=(num1, num2))
square_thread = threading.Thread(target=square, args=(arr,))
cube_thread = threading.Thread(target=cube, args=(arr,))

# Start all threads
addition_thread.start()
subtract_thread.start()
multiplication_thread.start()
square_thread.start()
cube_thread.start()

# Wait for all threads to complete
addition_thread.join()
subtract_thread.join()
multiplication_thread.join()
square_thread.join()
cube_thread.join()

print("All operations completed.")
'''
#Single thread in python
import threading
import time

def square(num):
    for n in num:
        time.sleep(0.1)
        print("Square is :",n*n)
def cube(num):
    for n in num:
        time.sleep(0.1)
        print("Cube is: ",n*n*n)

#Array for square and cube function
arr=[4,6,2,9,1,3]

square(arr)
cube(arr)
print("All the operations of square and cube are completed.")

#Fibonnaci series
def fibonacci(n):
    fibonacci=[]
    
    a,b = 0,1
    for i in range(n):
        fibonacci.append(a)
        a,b = b,a +b
    return fibonacci
#Taking input from the user
terms = int(input("Enter the number of terms"))
#Generate the fibonnaci series
fibonacci = fibonacci(terms)
#Print the fibonnaci series
print("Fibonnaci series: ")
for num in fibonacci:
    print(num,end =" ")
        




