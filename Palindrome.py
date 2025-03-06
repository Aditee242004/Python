def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]

input_str = "This is a Simple String"
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
