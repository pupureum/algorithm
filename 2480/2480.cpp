#include <iostream>
using namespace std;

int get_max(int a, int b, int c)
{
	int max;

	if (a > b && a > c)
		return (a);
	else if (b > a && b > c)
		return (b);
	else
		return (c);
}

int main(void)
{
	int a, b, c, reward;

	cin >> a >> b >> c;

	if (a == b && b == c)
		reward = 10000 + a * 1000;
	else if (a != b && b != c && a != c)
		reward = 100 * get_max(a, b, c);
	else 
	{
		if (a == b && b != c)
			reward = 1000 + a * 100;
		else if (b == c && a != b)
			reward = 1000 + b * 100;
		else
			reward = 1000 + c * 100;
	} 
	cout << reward << endl;
	return (0);
}