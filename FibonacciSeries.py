def fibonacci(n):
    """Function to print Fibonacci series up to n terms"""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print() 

num_terms = int(input("Enter the number of terms: "))
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    fibonacci(num_terms)
