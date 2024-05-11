#include <stdio.h>

int max_k(int n) {
    int k = n - 1;
    int result = n;
    while (k >= 1 && result != 0) {
        result &= k;
        k -= 1;
    }
    return k + 1;
}

int main() {
    int t, n;
    scanf("%d", &t);

    while (t--) {
        scanf("%d", &n);
        printf("%d\n", max_k(n));
    }

    return 0;
}
