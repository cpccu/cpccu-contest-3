#include <stdio.h>

int can_make_x(int x) {
    while (x >= 111) {
        if (x % 11 == 0 || x % 111 == 0 || x % 1111 == 0 || x % 11111 == 0 || x % 111111 == 0 || x % 1111111 == 0 || x % 11111111 == 0 || x % 111111111 == 0) {
            return 1;
        }
        x -= 111;
    }
    return x == 0;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int x;
        scanf("%d", &x);
        
        if (can_make_x(x)) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}
