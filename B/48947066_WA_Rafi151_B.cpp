#include <stdio.h>
#include <string.h>

int countZeros(char *s, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') {
            count++;
        }
    }
    return count;
}

int isPalindrome(char *s, int n) {
    int i = 0;
    int j = n - 1;
    while (i < j) {
        if (s[i] != s[j]) {
            return 0;
        }
        i++;
        j--;
    }
    return 1;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        char s[n+1];
        scanf("%s", s);

        int aliceDollars = 0;
        int bobDollars = 0;
        int palindrome = 1;

        while (countZeros(s, n) > 0) {
            if (palindrome) {
                if (s[n/2] == '0') {
                    s[n/2] = '1';
                    aliceDollars++;
                } else {
                    int i = 0;
                    while (s[i] == '1') {
                        i++;
                    }
                    s[i] = '1';
                    aliceDollars++;
                }
            } else {
                if (s[n/2] == '0') {
                    s[n/2] = '1';
                    bobDollars++;
                } else {
                    int i = n - 1;
                    while (s[i] == '1') {
                        i--;
                    }
                    s[i] = '1';
                    bobDollars++;
                }
            }
            palindrome = isPalindrome(s, n);
        }

        if (aliceDollars < bobDollars) {
            printf("ALICE\n");
        } else if (aliceDollars > bobDollars) {
            printf("BOB\n");
        } else {
            printf("DRAW\n");
        }
    }

    return 0;
}
