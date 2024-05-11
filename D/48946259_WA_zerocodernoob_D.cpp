#include <iostream>

using namespace std;

bool can_make_x(int x) {
    if (x % 11 == 0 || x % 111 == 0 || x % 1111 == 0 || x % 11111 == 0 || x % 111111 == 0 || x % 1111111 == 0 || x % 11111111 == 0 || x % 111111111 == 0) {
        return true;
    }

    for (int i = 1; i <= 9; ++i) {
        for (int j = 1; j <= 9; ++j) {
            if (i * 111111111 + j * 11111111 == x) {
                return true;
            }
        }
    }

    return false;
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int x;
        cin >> x;
        if (can_make_x(x)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
