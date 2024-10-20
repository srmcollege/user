def fibonacci(n):
    fibonacci=[]
    a,b = 0,1
    for i in range(n):
        fibonacci.append(a)
        a,b = b,a +b
    return fibonacci
terms = int(input("Enter the number of terms"))
fibonacci = fibonacci(terms)
print("Fibonnaci series: ")
for num in fibonacci:
    print(num,end ="  ")
