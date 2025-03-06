def display_menu():
    print("\nDictionary Operations:")
    print("1. Display Keys")
    print("2. Display Values")
    print("3. Display Key-Value Pairs")
    print("4. Get Value for a Key")
    print("5. Remove a Key-Value Pair")
    print("6. Exit")

def main():
    my_dict = {'name': 'Aditee', 'age': 21, 'city': 'Pune', 'job': 'Software Engineer'}

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("Keys:", list(my_dict.keys()))

        elif choice == '2':
            print("Values:", list(my_dict.values()))

        elif choice == '3':
            print("Key-Value Pairs:", list(my_dict.items()))

        elif choice == '4':
            key = input("Enter key to get value: ")
            print(f"Value for '{key}':", my_dict.get(key, "Key not found"))

        elif choice == '5':
            key = input("Enter key to remove: ")
            if key in my_dict:
                removed_value = my_dict.pop(key)
                print(f"Removed: {key} -> {removed_value}")
            else:
                print("Key not found!")

        elif choice == '6':
            print("Exit...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
