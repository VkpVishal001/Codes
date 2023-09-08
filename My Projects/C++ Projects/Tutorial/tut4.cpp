#include<iostream>

int a = 8;

void sub1(){
    int a = 3;
    std::cout<<a; 
}

void sub2(){
    std::cout<<a; 
}

int main(){
    int a = 5;
    sub1();
    sub2();
    std::cout<<a;
    return 0;
}