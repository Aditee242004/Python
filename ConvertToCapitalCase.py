def alternate_capitalization(s):
    result = ""
    for i, char in enumerate(s):
        if char.isalpha(): 
            result += char.upper() if i % 2 == 0 else char.lower()
        else:
            result += char 
    return result

input_str = input("Enter a string: ")
output_str = alternate_capitalization(input_str)
print("Output:", output_str)
