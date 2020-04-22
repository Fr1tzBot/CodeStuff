#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;
int main() {
    int foo = 8;
    char aString[100] = "yeet";
    string firstName;
    cout << "Type your first name: ";
    getline(cin, firstName); // get user input from the keyboard
    cout << "Nice To Meet You, " << firstName;
    return 0;
}