#include<bits/stdc++.h>
using namespace std;

bool isPalindrome(const string & s){
    int l=0,r=s.length()-1;
    while(l<r)
    {
        if(s[l]!=s[r])
            return false;
        l++;
        r--;
    }
    return true;
}

int main(){
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;

        int aliceDollars=0,bobDollars=0;
        bool aliceTurn=true;

        while(s.find('0')!=string::npos)
        {
            if(aliceTurn)
            {
                int index=s.find('0');
                s[index]='1';
                aliceDollars++;
            }
            else{
                if(!isPalindrome(s))
                {
                    reverse(s.begin(), s.end());
                    bobDollars++;
                }
                else{
                    int index=s.find('0');
                    s[index]='1';
                    aliceDollars++;
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
