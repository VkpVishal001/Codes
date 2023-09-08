#include<iostream>
/*
This line helps us to import a file named 'iostream' , which contains functions like cout .
*/

int main(){
    std::cout<<"Hello World";
    return 0;
}

/*
'int' in line 6 refers to the type of result it will get after successfully running the program (because it returns 0 at the end) .

main() is the name of the main function (if any other function is used as the main function , it will return an error) .

std refers to the namespace of cout , which is imported from 'iostream' .

'cout' function prints any string/value provided to it .

return 0 is written to provide a message to the program that it is successfully terminated .
*/