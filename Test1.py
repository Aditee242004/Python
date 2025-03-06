def display_menu():
    print("\nTuple Operations:")
    print("1. Get Length of Tuple")
    print("2. Find Maximum Element")
    print("3. Find Minimum Element")
    print("4. Count Occurrences of an Element")
    print("5. Find Index of an Element")
    print("6. Exit")

def main():
    my_tuple = (5, 10, 15, 20, 10, 25, 10, 30)

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(f"Length of tuple: {len(my_tuple)}")

        elif choice == '2':
            print(f"Maximum element: {max(my_tuple)}")

        elif choice == '3':
            print(f"Minimum element: {min(my_tuple)}")

        elif choice == '4':
            element = int(input("Enter element to count: "))
            print(f"Count of {element}: {my_tuple.count(element)}")

        elif choice == '5':
            element = int(input("Enter element to find index: "))
            if element in my_tuple:
                print(f"Index of {element}: {my_tuple.index(element)}")
            else:
                print(f"{element} not found in tuple.")

        elif choice == '6':
            print("Quit...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
