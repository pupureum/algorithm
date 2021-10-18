#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int n;

    cin >> n;
    for(int i = n; i > 0; i--)
    {
        cout << i << "\n";; //endl을 사용하면 버퍼 비워내야해서 시간초과 뜬다.
    }
    return (0);
}
