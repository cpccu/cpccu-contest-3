#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        string s;
        cin >> s;

        int aliceDollars = 0, bobDollars = 0;
        int i = 0, j = n - 1;
        bool lastOperationWasReverse = false;

        while (i <= j) {
            if (s[i] == '0') {
                if (i == j) {
                    aliceDollars++;
                } else {
                    s[i] = '1';
                }
            }

            if (s[j] == '0') {
                if (i != j) {
                    s[j] = '1';
                }
            }

            if (!lastOperationWasReverse && !equal(s.begin(), s.end(), s.rbegin())) {
                reverse(s.begin(), s.end());
                lastOperationWasReverse = true;
            } else {
                lastOperationWasReverse = false;
            }

            i++;
            j--;
        }

        if (aliceDollars < bobDollars) {
            cout << "ALICE" << endl;
        } else if (aliceDollars > bobDollars) {
            cout << "BOB" << endl;
        } else {
            cout << "DRAW" << endl;
        }
    }

    return 0;
}
