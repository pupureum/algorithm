#include <iostream>
using namespace std;

int check_exception(int a, int b, int c)
{
	if (b >= c)
	{
		cout << "-1";
		return (1);
	}
	else if (c - b == 1)
	{
		cout << a + 1;
		return (1);
	}
	return (0);
}

int main(void)
{
	int a, b, c, n = 0;
	
	cin >> a >> b >> c;
	if (check_exception(a, b, c) != 1)
	{
		n = a / (c - b) + 1;
		cout << n;
	}
	return (0);
}