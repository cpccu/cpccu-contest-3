#include <stdio.h>

// Function to check if r can be made using the numbers 11 and 111
char* can_make_r(int r) {
    // If r is greater than or equal to 111, it can always be made
    if (r >= 111) {
        return "YES";
    } else {
        // Otherwise, check if it can be made using a combination of 11s and 111s
        for (int i = 0; i <= r / 11; i++) {
            if ((r - 11 * i) % 111 == 0) {
                return "YES";
            }
        }
    }
    return "NO";
}

int main() {
    int t;
    scanf("%d", &t);

    // Process each test case
    for (int i = 0; i < t; i++) {
        int r;
        scanf("%d", &r);
        char* result = can_make_r(r);
        printf("%s\n", result);
    }

    return 0;
}
