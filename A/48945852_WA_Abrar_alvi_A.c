#include <stdio.h>
#include <math.h>

int max_k(int n) {
    if (n == 1) {
        return 1;
    } else {
        int power_of_2 = 1 << (int)(log2(n));
        return power_of_2;
    }
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        int n;
        scanf("%d", &n);
        int result = max_k(n);
        printf("%d\n", result);
    }

    return 0;
}
