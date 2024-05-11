#include <stdio.h>
#include <string.h>

#define MAX_N 1005

char s[MAX_N];

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);
        scanf("%s", s);

        int alice_cost = 0, bob_cost = 0;
        int alice_turn = 1;

        int i = 0, j = n - 1;
        while (i <= j) {
            if (s[i] != '1' && s[j] != '1') {
                if (s[i] != s[j]) {
                    if (alice_turn) {
                        s[j] = '1';
                        alice_cost++;
                    } else {
                        s[i] = '1';
                        bob_cost++;
                    }
                } else {
                    if (alice_turn)
                        alice_cost++;
                    else
                        bob_cost++;
                }
            } else if (s[i] != '1') {
                s[j] = '1';
                alice_cost++;
            } else if (s[j] != '1') {
                s[i] = '1';
                bob_cost++;
            }

            alice_turn = !alice_turn;
            i++;
            j--;
        }

        if (alice_cost < bob_cost)
            printf("ALICE\n");
        else if (alice_cost > bob_cost)
            printf("BOB\n");
        else
            printf("DRAW\n");
    }

    return 0;
}
