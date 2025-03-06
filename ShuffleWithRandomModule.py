import random

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(numbers)  # Shuffle the list in place

    print("Shuffled List:")
    for num in numbers:
        print(num)
