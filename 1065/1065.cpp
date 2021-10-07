#include <iostream>
using namespace std;

bool	is_han(int n)
{
	int a, b, c;

	c = n % 10;
	n /= 10;
	b = n % 10;
	n /= 10;
	a = n;
	if ((b - a) == (c - b))
		return (true);
	else
		return (false);
}

int main(void)
{
	int n, cnt;

	cin >> n;
	cnt = 0;
	if (n < 111)
		{
			if (n <= 99)
				cout << n << endl;
			else
				cout << 99 << endl;
		}
	else
	{
		for (int i = 111; i <= n; i++)
		{
			if (is_han(i) == true)
				cnt++;
		}
		cout << cnt + 99 << endl;
	}
	return (0);
}