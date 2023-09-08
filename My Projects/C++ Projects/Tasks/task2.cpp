/* Task 2 : Using if-else in C++ */

#include<iostream>

using namespace std;

int main(){
    cout<<"Enter your age : ";

    int a;
    cin>>a;

    if (a<18)
    {
        cout<<"You are not eligible to vote";
    }

    else
    {
        cout<<"You are eligible to vote";
    }

    return 0;
    
}