#include <iostream>
using namespace std;

int getNum(int k, int n)
{
	if (n == 1)
		return (1);
	if (k == 0)
		return (n);
	return (getNum(k - 1, n) + getNum(k, n - 1));
}

int main(void)
{
	int num, k, n;

	cin >> num;
	for (int i = 0; i < num; i++)
	{
		cin >> k >> n;
		cout << getNum(k, n) << endl;
	}

	return (0);
}