#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> potions(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> potions[i];
    }

    int count = 0;
    int current_health = 0;

    for (int i = 0; i < n; ++i) {
        if (current_health + potions[i] >= 0) {
            current_health += potions[i];
            count++;
        }
    }

    std::cout << count << std::endl;

    return 0;
}
