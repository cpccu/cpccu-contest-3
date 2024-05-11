#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isPalindrome(const string& s) {
    int n = s.length();
    for (int i = 0; i < n / 2; ++i) {
        if (s[i] != s[n - i - 1]) {
            return false;
        }
    }
    return true;
}

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
                // Alice's turn
                if (i == j) {
                    aliceDollars++;
                } else {
                    s[i] = '1';
                }
            }

            if (s[j] == '0') {
                // Bob's turn
                if (i != j) {
                    s[j] = '1';
                }
            }

        
            if (!isPalindrome(s) && !lastOperationWasReverse) {
                bobDollars++;
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
