#include <stdio.h>

// Function to check if x can be made using a combination of 1, 11, 111, ...
int can_make_x(int x) {
    // Iterate through each possible number of 1s
    for (int i = 1; i < 10; i++) {
        int num = 0;
        // Create the number with i 1s
        for (int j = 0; j < i; j++) {
            num = num * 10 + 1;
        }
        // If x is divisible by the current number of 1s, we can make x
        if (x % num == 0) {
            return 1;
        }
    }
    return 0;
}

int main() {
    int t;
    // Read the number of test cases
    scanf("%d", &t);

    // Iterate over each test case
    while (t--) {
        int x;
        // Read the input x for each test case
        scanf("%d", &x);

        // Check if x can be made using a combination of 1, 11, 111, ...
        if (can_make_x(x)) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}
