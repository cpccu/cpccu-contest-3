#include <iostream>

using namespace std;

string canMakeX(int x) {
    int currentNumber = 11;
    while (currentNumber <= x) {
        if (x % currentNumber == 0) {
            return "YES";
        }
        currentNumber = currentNumber * 10 + 1;
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
