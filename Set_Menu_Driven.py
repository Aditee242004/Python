def display_menu():
    print("\nSet Operations Menu:")
    print("1. Add an element")
    print("2. Remove an element")
    print("3. Union of two sets")
    print("4. Intersection of two sets")
    print("5. Difference of two sets")
    print("6. Check subset")
    print("7. Display set")
    print("8. Exit")

# Initialize an empty set
my_set = set()

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to add: ")
        my_set.add(element)
        print("Updated Set:", my_set)

    elif choice == 2:
        element = input("Enter element to remove: ")
        if element in my_set:
            my_set.remove(element)  # Raises error if element not found
            print("Updated Set:", my_set)
        else:
            print("Element not found in set.")

    elif choice == 3:
        another_set = set(input("Enter elements of another set (space-separated): ").split())
        union_set = my_set.union(another_set)
        print("Union:", union_set)

    elif choice == 4:
        another_set = set(input("Enter elements of another set (space-separated): ").split())
        intersection_set = my_set.intersection(another_set)
        print("Intersection:", intersection_set)

    elif choice == 5:
        another_set = set(input("Enter elements of another set (space-separated): ").split())
        difference_set = my_set.difference(another_set)
        print("Difference:", difference_set)

    elif choice == 6:
        another_set = set(input("Enter elements of another set (space-separated): ").split())
        if my_set.issubset(another_set):
            print("The set is a subset of the given set.")
        else:
            print("The set is not a subset.")

    elif choice == 7:
        print("Current Set:", my_set)

    elif choice == 8:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
3