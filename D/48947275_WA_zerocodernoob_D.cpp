#include <iostream>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int x;
        std::cin >> x;

        if (x % 11 == 0 && x >= 11 * (x / 11)) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }

    return 0;
}
