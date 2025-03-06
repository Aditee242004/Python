def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char in consonants)
    
    return vowel_count, consonant_count

input_str = "This is a Simple String"
vowels, consonants = count_vowels_consonants(input_str)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
