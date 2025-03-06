def remove_duplicate_words(s):
    words = s.split()
    unique_words = list(dict.fromkeys(words))
    return " ".join(unique_words)

input_string = input("Enter a string:\n")
result = remove_duplicate_words(input_string)

print("String after removing duplicate words:")
print(result)
