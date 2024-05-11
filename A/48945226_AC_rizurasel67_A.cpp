#include<bits/stdc++.h>
using namespace std;

int findMaxK(int n){
    int hp2=1;
    while(hp2<=n)
    {
        hp2<<=1;
    }
    return hp2>>1;
}

int main(){
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        cout<<findMaxK(n)-1<<endl;
    }
    return 0;
}
