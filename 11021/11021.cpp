#include <iostream>
using namespace std;

int main(void)
{
    int n, a, b, sum;

    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        sum = 0;
        cin >> a >> b;
        sum = a + b;
        cout << "Case #" << i << ": " << sum << "\n";
    }
    return (0);
}