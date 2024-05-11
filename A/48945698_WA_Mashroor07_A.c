#include <stdio.h>

int find_max_k(int n) {
    int a = n;
    while ((a & (a - 1)) != 0) 
{
        a--;
    }
    return a;
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
