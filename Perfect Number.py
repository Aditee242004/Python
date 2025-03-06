def is_perfect_number(num):
    if num < 1:
        return False
    
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    
    return sum_of_divisors == num

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
