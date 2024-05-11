#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define ll long long
#define PI 3.1416

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		int ans = n;
		while (n--) {
			ans &= n;
			if (ans == 0) {
				cout << n << '\n';
				break;
			}
		}
	}
	return 0;
}	