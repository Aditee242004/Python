
numbers = [5, 15, 20, 25, 30, 20, 40]

if 20 in numbers:
    index = numbers.index(20)  
    numbers[index] = 10        # Replace it with 10

# Display the updated list
print("Updated List:\n")
for num in numbers:
    print(num)
