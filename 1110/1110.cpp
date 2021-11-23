#include <iostream>
using namespace std;

int main(void)
{
	int n = 0, input, result;

	cin >> input;
	result = input;
	do
	{
		result = (result % 10) * 10 + ((result / 10 + result % 10) % 10);
		n++;
	}
	while (result != input);
	cout << n;
	return (0);
}