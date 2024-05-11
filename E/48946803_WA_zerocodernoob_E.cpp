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
        }
    }

    std::cout << count << std::endl;

    return 0;
}
