#include <iostream>

using namespace std;

string canMakeX(int x) {
    if (x % 11 == 0 || (x % 1111111111 == 0 && x >= 1111111111)) {
        return "YES";
    }
    return "NO";
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int x;
        cin >> x;

        string result = canMakeX(x);

        cout << result << endl;
    }

    return 0;
}
