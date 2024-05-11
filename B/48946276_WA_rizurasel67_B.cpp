#include<bits/stdc++.h>
using namespace std;

bool isPalindrome(const string& s){
    int left=0,right=s.length()-1;
    while (left<right){
        if(s[left]!=s[right])
            return false;
        left++;
        right--;
    }
    return true;
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;

        int aliceDollars=0,bobDollars=0;

        bool aliceTurn=true;
        while(s.find('0')!=string::npos){
            if(aliceTurn){
                int index=s.find('0');
                s[index]='1';
                aliceDollars++;
            } else{
                if(isPalindrome(s)){
                    int index=s.find('0');
                    s[index]='1';
                    aliceDollars++;
                }else{
                    reverse(s.begin(),s.end());
                    bobDollars++;
                }
            }
            aliceTurn=!aliceTurn;
        }

        
        if(aliceDollars<bobDollars)
            cout<<"ALICE\n";
        else if(aliceDollars>bobDollars)
            cout<<"BOB\n";
        else
            cout<<"DRAW\n";
    }
    return 0;
}
