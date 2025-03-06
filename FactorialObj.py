class Factorial:
    def __init__(self, number):
        self.number = number

    def calculate_factorial(self):
        if self.number < 0:
            return "Factorial is not defined for negative numbers."
        elif self.number == 0 or self.number == 1:
            return 1
        else:
            fact = 1
            for i in range(1, self.number + 1):
                fact *= i
            return fact


def main():
    try:
        num = int(input("Enter a number to find its factorial: "))
        factorial_object = Factorial(num)
        result = factorial_object.calculate_factorial()
        print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
