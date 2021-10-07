#include <iostream>
using namespace std;

int main(void)
{
	int num, remainder[42] = {0}, cnt;

	cnt = 0;
	for (int i = 0; i < 10; i++)
	{
		cin >> num;
		if (!remainder[num % 42]++)
			cnt++;
	}
	cout << cnt << endl;
	return (0);
}