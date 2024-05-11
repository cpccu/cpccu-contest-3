#include <iostream>
#include <vector>
using namespace std;

string play_game(int n, string s) {
    int alice_dollars = 0;
    int bob_dollars = 0;
    int i = 0, j = n - 1;
    bool last_operation_was_reverse = false;

    while (i <= j) {
        if (s[i] == '0') {
            if (i == j) {
                alice_dollars += 1;
            } else {
                s[i] = '1';
            }
        }

        if (s[j] == '0') {
            if (i != j) {
                s[j] = '1';
            }
        }

        if (!last_operation_was_reverse && s[i] == '0' && s[j] == '0') {
            bob_dollars += 1;
            reverse(s.begin(), s.end());
            last_operation_was_reverse = true;
        } else {
            last_operation_was_reverse = false;
        }

        i += 1;
        j -= 1;
    }

    if (alice_dollars < bob_dollars) {
        return "ALICE";
    } else if (alice_dollars > bob_dollars) {
        return "BOB";
    } else {
        return "DRAW";
    }
}

int main() {
    int t;
    cin >> t;

    for (int testCase = 0; testCase < t; ++testCase) {
        int n;
        cin >> n;

        string s_input;
        cin >> s_input;

        string result = play_game(n, s_input);
        cout << result << endl;
    }

    return 0;
}
