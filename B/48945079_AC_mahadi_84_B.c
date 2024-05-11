#include <stdio.h>
#include <string.h>

#define MAXN 1005

char s[MAXN];

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        scanf("%s", s);

        int cntZero = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                cntZero++;
            }
        }

        if (cntZero == 1) {
            printf("BOB\n");
            continue;
        }

        if (cntZero % 2 == 0) {
            printf("BOB\n");
        } else {
            printf("ALICE\n");
        }
    }
    return 0;
}
