#include <stdio.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t); // Input number of test cases

    while (t--) {
        int n;
        char s[1005];
        scanf("%d", &n); // Input length of string
        scanf("%s", s); // Input the string

        // Count the number of '1's in the string
        int count_ones = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                count_ones++;
            }
        }

        // If the count of '1's is odd and greater than 1, Alice wins
        // If the count of '1's is even or 1, Bob wins
        // If there's only one character, it's a draw
        if (count_ones % 2 == 1 && count_ones > 1) {
            printf("ZICE\n");
        } else if (count_ones == 1 || count_ones % 2 == 0) {
            printf("30B\n");
        } else {
            printf("DRAW\n");
        }
    }

    return 0;
}
