#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> potions(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> potions[i];
    }

    long long current_sum = 0;
    long long max_sum = 0;

    for (int i = 0; i < n; ++i) {
        current_sum += potions[i];
        if (current_sum < 0) {
            current_sum = 0;
        }
        max_sum = std::max(max_sum, current_sum);
    }

    std::cout << max_sum << std::endl;

    return 0;
}
