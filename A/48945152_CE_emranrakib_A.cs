#include <stdio.h>

int max_k(int n) {
    if (n == 1)
        return 0;

    int left = 0, right = n, result = 0;

    while (left <= right) {
        int mid = (left + right) / 2;
        if ((n & (n - 1)) & (n & (n - 1) - 1) & (n & (n - 1) & (n - 2)) & (n & (n - 1) & (n - 2) & (n - 3)) & mid == 0) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        printf("%d\n", max_k(n));
    }

    return 0;
}

