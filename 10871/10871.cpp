#include <iostream>
using namespace std;

int	main(void)
{
	int	num, max, iter;

	cin >> iter >> max;
	for (int i = 0; i < iter; i++)
	{
		cin >> num;
		if (num < max)
			cout << num << ' ';
	}
	return (0);
}
