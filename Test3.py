def count_vowel_occurrences(s):
    vowels = "AEIOUaeiou"
    vowel_count = {v: 0 for v in vowels} 

    for char in s:
        if char in vowel_count:
            vowel_count[char] += 1

    vowel_count = {k: v for k, v in vowel_count.items() if v > 0}

    return vowel_count

input_string = input("Enter a string: ")

result = count_vowel_occurrences(input_string)
print("\nVowel Occurrences:")
for vowel, count in result.items():
    print(f"{vowel}: {count}")
