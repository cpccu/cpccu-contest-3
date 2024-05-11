#include <iostream>
#include <string>
using namespace std;

string ans(int n) {
    while (n > -1) {
        n -= 11;
        string s = to_string(n);
        if ((s.find('1') != string::npos && s.size() == 1) || n == 0) {
            return "YES";
        }
    }
    return "NO";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << ans(n) << endl;
    }
    return 0;
}
