#include <iostream>
using namespace std;

int main(void)
{
	int  num, result = 0;

	cin >> num;
	if (num == 1)
		result = 1;
	else
	{
		for (int sum = 1; sum < num; result++)
			sum += 6 * result;
	}
	cout << result << endl;
	return (0);
}