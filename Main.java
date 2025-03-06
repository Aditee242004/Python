import java.util.Scanner;

class StringManipulator {
    private String text;

    // Method to input the string from the user
    public void inputString() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        text = scanner.nextLine();
    }

    // Method to display the string in uppercase
    public void displayUpperCase() {
        if (text != null) {
            System.out.println("Uppercase String: " + text.toUpperCase());
        } else {
            System.out.println("No string entered.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        StringManipulator sm = new StringManipulator();
        sm.inputString();
        sm.displayUpperCase();
    }
}
