import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt(); 
            int maxK = findMaxK(n);
            System.out.println(maxK);
        }
        
        scanner.close();
    }
    
    public static int findMaxK(int n) {
        int k = n;
        while ((k & (k - 1)) != 0) { 
            k &= k - 1;
        }
        return k - 1;
    }
}
