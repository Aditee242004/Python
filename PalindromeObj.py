class PalindromeNumber:
    def __init__(self, number):
        self.number = number

    def is_palindrome(self):
        return str(self.number) == str(self.number)[::-1]


def main():
    try:
        num = int(input("Enter a number to check if it's a palindrome: "))
        palindrome_object = PalindromeNumber(num)
        result = palindrome_object.is_palindrome()
        if result:
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
