import threading
from time import sleep

def addition(num1, num2):
    num3 = num1 + num2
    print(f"Addition is {num3}")
    sleep(1)

def subtraction(num1, num2):
    num3 = num1 - num2
    print(f"Subtraction is {num3}")
    sleep(1)

def multiplication(num1, num2):
    num3 = num1 * num2
    print(f"Multiplication is {num3}")
    sleep(1)

def square(nums):
    for num in nums:
        sleep(1)
        print(f"Square of number {num} is {num * num}")

def cube(nums):
    for num in nums:
        sleep(1)
        print(f"Cube of number {num} is {num * num * num}")

# Input from user
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter integer values.")
    exit(1)

arr = [2, 3, 4, 6]

addition_thread = threading.Thread(target=addition, args=(num1, num2))
subtraction_thread = threading.Thread(target=subtraction, args=(num1, num2))
multiplication_thread = threading.Thread(target=multiplication, args=(num1, num2))
square_thread = threading.Thread(target=square, args=(arr,))
cube_thread = threading.Thread(target=cube, args=(arr,))

addition_thread.start()
subtraction_thread.start()
multiplication_thread.start()
square_thread.start()
cube_thread.start()

addition_thread.join()
subtraction_thread.join()
multiplication_thread.join()
square_thread.join()
cube_thread.join()

print("All threads have completed their tasks.")
