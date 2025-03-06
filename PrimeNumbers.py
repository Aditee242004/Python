def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    print("Prime Numbers:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

start = int(input("Enter the first range: "))
end = int(input("Enter the last range: "))

print()
print_primes_in_range(start, end)
