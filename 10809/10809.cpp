#include <iostream>
#include <string.h>
using namespace std;

int main(void)
{
    string str;
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    cin >> str;
    for (int i = 0; i < alphabet.length(); i++)
        cout << (int)str.find(alphabet[i]) << " ";
    cout << endl; 
    return (0);
}
