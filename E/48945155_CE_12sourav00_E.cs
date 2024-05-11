#include <stdio.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

int maxPotions(int n, int potions[]) {
    int dp[n + 1]; // Dynamic programming array to store the maximum number of potions that can be drunk up to each position
    dp[0] = 0; // Base case, no potions are drunk
    dp[1] = max(0, potions[0]); 
    
    
    for (int i = 2; i <= n; i++) {
       \
        dp[i] = max(dp[i - 1], dp[i - 2] + max(0, potions[i - 1]));
    }
    
    return dp[n]; 
}

int main() {
    int n;
    scanf("%d", &n); 
    
    int potions[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &potions[i]);
    }
    
    printf("%d\n", maxPotions(n, potions));     
    return 0;
}
