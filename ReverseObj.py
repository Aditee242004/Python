class ReverseNumber:
    def __init__(self, number):
        self.number = number

    def calculate_reverse(self):
        rev = 0
        temp = self.number
        while temp > 0:
            remainder = temp % 10
            rev = (rev * 10) + remainder
            temp //= 10
        return rev


def main():
    try:
        num = int(input("Enter a number to find its reverse: "))
        reverse_object = ReverseNumber(num)
        result = reverse_object.calculate_reverse()
        print(f"The reverse of {num} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()

