#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> potions(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> potions[i];
    }

    long long current_health = 0;
    long long max_potions = 0;

    for (int i = 0; i < n; ++i) {
        if (current_health + potions[i] >= 0) {
            current_health += potions[i];
            max_potions++;
        }
    }

    std::cout << max_potions << std::endl;

    return 0;
}
