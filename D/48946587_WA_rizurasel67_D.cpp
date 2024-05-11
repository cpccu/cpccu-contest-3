#include<bits/stdc++.h>
using namespace std;

bool canMakeNumber(int x){
    return x%11<=to_string(x).length();
}

int main(){
    int t;
    cin>>t;

    while(t--)
    {
        int x;
        cin>>x;

        if(canMakeNumber(x))
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }

    return 0;
}
