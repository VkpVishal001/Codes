#include<iostream>

using namespace std;

int main(){

    cout<<"C++ Operators :- "<<endl<<endl;
    cout<<"Arithmetic Operators : "<<endl<<endl;

    int a, b;

    cout<<"Enter the value of a : ";
    cin>>a;

    cout<<"Enter the value of b : ";
    cin>>b;
    cout<<endl;

    cout<<"a + b : "<<(a+b)<<endl;
    cout<<"a - b : "<<(a-b)<<endl;
    cout<<"a * b : "<<(a*b)<<endl;
    cout<<"a / b : "<<(a/b)<<endl;
    cout<<"a ++  : "<<(a++)<<endl;
    cout<<"a --  : "<<(a--)<<endl;
    cout<<" ++a  : "<<(++a)<<endl;
    cout<<" --a  : "<<(--a)<<endl<<endl;

    cout<<"Assignment Operators : ="<<endl<<endl;

    cout<<"Comparison Operators : == , =! , < , > , <= , >="<<endl<<endl;

    cout<<"Logical Operators : && (and) , || (or) , ! (not)"<<endl<<endl;
    return 0;
}
