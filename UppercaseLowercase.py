def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    return upper_count, lower_count

input_str = input("Enter a string: ")
upper, lower = count_upper_lower(input_str)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
