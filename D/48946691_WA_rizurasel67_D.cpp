#include <iostream>
using namespace std;

bool canMakeNumber(int x) {
    while (x > 0) {
        if (x % 11 == 0)
            return true;
        x -= 111;
    }
    return false;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int x;
        cin >> x;

        if (canMakeNumber(x))
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
