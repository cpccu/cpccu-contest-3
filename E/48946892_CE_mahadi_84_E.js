#include <stdio.h>

#define MAXN 2005

int potions[MAXN];

int main() {
    int n;
    scanf("%d", &n);

  
    for (int i = 0; i < n; ++i) {
        scanf("%d", &potions[i]);
    }

    int health = 0; 
    int maxPotions = 0;

    
    for (int i = 0; i < n; ++i) {
       
        if (health + potions[i] >= 0) {
            health += potions[i]; 
            maxPotions++;
        }
    }

    printf("%d\n", maxPotions); 

    return 0;
}
