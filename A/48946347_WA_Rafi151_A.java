import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int t = scanner.nextInt(); // Read the number of test cases
        
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt(); // Read the value of n for each test case
            int k = findK(n); // Calculate the required integer k
            System.out.println(k); // Output the result for each test case
        }
        
        scanner.close();
    }
    
    // Function to calculate the required integer k
    private static int findK(int n) {
        int k = 1;
        while (k <= n) {
            k *= 2; // Double k until it exceeds n
        }
        return k - 1; // Subtract 1 to get the largest k such that k < n
    }
}
