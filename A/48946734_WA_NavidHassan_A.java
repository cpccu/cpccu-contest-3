import java.util.Scanner;

public class Main {

    public static int findMaximumK(int n) {

        int leftmostSetBit = 0;
        while ((1 << leftmostSetBit) <= n) {
            leftmostSetBit++;
        }

        int result = (1 << leftmostSetBit) - 1;

        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int result = findMaximumK(n);
            System.out.println(result);
        }
    }
}
