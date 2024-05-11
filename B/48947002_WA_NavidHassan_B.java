import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            String s = scanner.next();
            String result = findWinner(n, s);
            System.out.println(result);
        }
    }

    public static String findWinner(int n, String s) {
        int aliceCost = 0;
        int bobCost = 0;

        for (int i = 0; i < n / 2; i++) {
            if (s.charAt(i) != '1') {
                aliceCost++;
            }
        }

        bobCost = aliceCost; // Bob will spend the same amount as Alice initially

        // Check if the game ends in a draw
        if (n % 2 == 1 && s.charAt(n / 2) == '0') {
            return "DRAW";
        }

        return (aliceCost > bobCost) ? "BOB" : "ALICE";
    }
}
