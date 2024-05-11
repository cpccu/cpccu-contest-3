#include <stdio.h>

int find_max_k(int n) {
    int k = n;
    while ((k & (k - 1)) != 0) {
        k--;
    }
    return k;
}

int main() {
    int t;
    scanf("%d", &t);
    
    while (t--) {
        int n;
        scanf("%d", &n);
        
        int max_k = find_max_k(n);
        
        printf("%d\n", max_k);
    }
    return 0;
}
