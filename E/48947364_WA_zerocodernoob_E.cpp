#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> potions(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> potions[i];
    }

    int health = 0;
    int count = 0;

    for (int i = 0; i < n; ++i) {
        if (health + potions[i] >= 0) {
            health += potions[i];
            count++;
        } else if (potions[i] >= 0) {
            int j = i - 1;
            while (j >= 0 && potions[j] < 0 && health < 0) {
                health -= potions[j];
                j--;
            }
            if (j >= 0 && potions[j] < 0) {
                health += potions[i] - potions[j];
                potions[j] = 0;
                count++;
            }
        }
    }

    std::cout << count << std::endl;

    return 0;
}
