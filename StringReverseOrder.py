def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

input_str = "This is a Simple String"
output_str = reverse_words(input_str)
print(output_str)
