#include <stdio.h>
#include <stdlib.h>

void find_permutation(int n, int *a) {
    int b[2 * n];
    int visited[2 * n];
    int i, j;

    for (i = 0; i < 2 * n; i++) {
        visited[i] = 0;
    }

    for (i = 0; i < 2 * n; i++) {
        if (!visited[i]) {
            visited[i] = 1;
            b[0] = a[i];
            int previous = a[i];
            for (j = 1; j < 2 * n; j++) {
                int possible_value = previous + 1;
                if (possible_value > 2 * n) {
                    possible_value -= 2 * n;
                }
                while (visited[possible_value - 1] || possible_value == previous) {
                    possible_value++;
                    if (possible_value > 2 * n) {
                        possible_value -= 2 * n;
                    }
                }
                b[j] = possible_value;
                visited[possible_value - 1] = 1;
                previous = possible_value;
            }
            break;
        }
    }

    for (i = 0; i < 2 * n; i++) {
        printf("%d ", b[i]);
    }
    printf("\n");
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        int *a = (int *)malloc(2 * n * sizeof(int));
        for (int i = 0; i < 2 * n; i++) {
            scanf("%d", &a[i]);
        }

        find_permutation(n, a);

        free(a);
    }

    return 0;
}
