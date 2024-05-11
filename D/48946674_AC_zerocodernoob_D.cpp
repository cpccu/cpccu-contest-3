#include <iostream>

using namespace std;

bool canMakeX(int x) {
    while (x >= 11) {
        if (x % 11 == 0 || x % 111 == 0) {
            return true;
        }
        x -= 111;
    }
    return false;
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int x;
        cin >> x;

        string result = canMakeX(x) ? "YES" : "NO";

        cout << result << endl;
    }

    return 0;
}
