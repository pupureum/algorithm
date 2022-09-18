#include <iostream>
using namespace std;

int isDecimal(int num)
{
	int cnt = 0;

	for (int i = 1; i <= num; i++)
	{
		if (num % i == 0)
			cnt++;
	}
	if (cnt == 2)
		return (true);
	else
		return (false);
}

int main(void)
{
	int n, input = 0, sum = 0;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> input;
		sum += isDecimal(input);
	}
	cout << sum << endl;
	return(0);
}