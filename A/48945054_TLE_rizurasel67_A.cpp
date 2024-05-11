#include<bits/stdc++.h>
using namespace std;

int findMaxK(int N){
    int k=N;
    while(k>0)
    {
        int result=N;
        for(int i=N-1;i>=k;i--)
        {
            result &=i;
            if(result==0)
                return k;
        }
        k--;
    }
    return 0;
}

int main(){
    int q;
    cin>>q;
    while(q--)
    {
        int n;
        cin>>n;
        cout<<findMaxK(n)<<endl;
    }
    return 0;
}
