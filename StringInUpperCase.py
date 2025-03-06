class StringManipulator:
    def __init__(self):
        self.text = ""

    # Method to input the string from the user
    def input_string(self):
        self.text = input("Enter a string: ")

    # Method to display the string in uppercase
    def display_uppercase(self):
        if self.text:
            print("Uppercase String:", self.text.upper())
        else:
            print("No string entered.")

if __name__ == "__main__":
    sm = StringManipulator()
    sm.input_string()
    sm.display_uppercase()