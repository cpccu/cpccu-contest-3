#include <iostream>

using namespace std;

int findMaximumK(int n) {
    int powerOfTwo = 1;
    while ((powerOfTwo * 2) <= n) {
        powerOfTwo *= 2;
    }
    return powerOfTwo - 1;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int result = findMaximumK(n);
        cout << result << endl;
    }

    return 0;
}
