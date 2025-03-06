import java.util.Scanner;

public class PrimeNumbers {
        static boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    static void printPrimesInRange(int start, int end) {
        System.out.println("Prime Numbers:");
        for (int i = start; i <= end; i++) {
            if (isPrime(i)) {
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first range: ");
        int start = scanner.nextInt();

        System.out.print("Enter the last range: ");
        int end = scanner.nextInt();

        System.out.println();
        printPrimesInRange(start, end);

        scanner.close();
    }
}
