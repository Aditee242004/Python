# Define a list
numbers = [5, 3, 8, 2, 1]

# Compare the first two elements
print(f"Before swapping: {numbers}")
if numbers[0] > numbers[1]:
    print(f"Swapping {numbers[0]} and {numbers[1]}")
    # Swap the elements
    numbers[0], numbers[1] = numbers[1], numbers[0]

print(f"After first swap: {numbers}")

# Perform Bubble Sort using comparison and swapping
n = len(numbers)
for i in range(n):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:  # Comparison
            print(f"Swapping {numbers[j]} and {numbers[j + 1]}")
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Swapping

print(f"Sorted list: {numbers}")

 