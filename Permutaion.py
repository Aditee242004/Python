import itertools

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    permutations = itertools.permutations(numbers)  # Generate all permutations

    for i, perm in enumerate(permutations):
     if i >= 10:  # Print only the first 10 permutations
        break
    print(perm)
