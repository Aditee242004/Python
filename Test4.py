def display_menu():
    print("\nList Operations:")
    print("1. Append an Element")
    print("2. Insert an Element at a Specific Position")
    print("3. Remove an Element")
    print("4. Pop an Element by Index")
    print("5. Sort the List")
    print("6. Display the List")
    print("7. Exit")

def main():
    my_list = [12,4,6,9,5,14] 

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            element = input("Enter element to append: ")
            my_list.append(element)
            print(f"{element} appended to the list.")

        elif choice == '2':
            element = input("Enter element to insert: ")
            index = int(input("Enter index position: "))
            if 0 <= index <= len(my_list):
                my_list.insert(index, element)
                print(f"{element} inserted at index {index}.")
            else:
                print("Invalid index!")

        elif choice == '3':
            element = input("Enter element to remove: ")
            if element in my_list:
                my_list.remove(element)
                print(f"{element} removed from the list.")
            else:
                print("Element not found!")

        elif choice == '4':
            index = int(input("Enter index to pop element: "))
            if 0 <= index < len(my_list):
                removed_element = my_list.pop(index)
                print(f"Element {removed_element} removed from index {index}.")
            else:
                print("Invalid index!")

        elif choice == '5':
            my_list.sort()
            print("List sorted successfully.")

        elif choice == '6':
            print("Current List:", my_list)

        elif choice == '7':
            print("Exit program...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
