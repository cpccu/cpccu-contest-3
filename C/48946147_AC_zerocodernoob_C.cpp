#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> arrange_array(int t, vector<pair<int, vector<int>>> &testcases) {
    vector<vector<int>> results;

    for (int i = 0; i < t; ++i) {
        int n = testcases[i].first;
        vector<int> a = testcases[i].second;
        sort(a.begin(), a.end());

        vector<int> b(2 * n, 0);

        for (int j = 0; j < n; ++j) {
            b[j * 2] = a[j];
        }

        for (int j = n; j < 2 * n; ++j) {
            b[(j - n) * 2 + 1] = a[j];
        }

        results.push_back(b);
    }

    return results;
}

int main() {
    int t;
    cin >> t;

    vector<pair<int, vector<int>>> testcases;
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        vector<int> a(2 * n);
        for (int j = 0; j < 2 * n; ++j) {
            cin >> a[j];
        }
        testcases.push_back({n, a});
    }

    vector<vector<int>> output = arrange_array(t, testcases);

    for (const auto &res : output) {
        for (int val : res) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
