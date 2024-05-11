#include <stdio.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

int main() {
    int n;
    scanf("%d", &n);

    int potions[n];
    for (int i = 0; i < n; ++i) {
        scanf("%d", &potions[i]);
    }

    int max_potions = 0;
    int health = 0;

    for (int i = 0; i < n; ++i) {
        health += potions[i];
        if (health >= 0) {
            max_potions++;
        } else {
            break;
        }
    }

    printf("%d\n", max_potions);

    return 0;
}
