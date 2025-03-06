class LinearSearch:
    @staticmethod
    def search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i  # Return the index of the found element
        return -1  # Return -1 if not found

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = int(input("Enter the number to search: "))
    result = LinearSearch.search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")
