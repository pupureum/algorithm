#include <iostream>
using namespace std;

int	main(void)
{
	int	i, num, a, b;

	i = 0;
	cin >> num;
	for(int i = 1; i <= num; i++)
	{
		cin >> a >> b;
		cout << "Case #" << i << ": " << a << " + " << b << " = " << a + b << '\n';
	}
	return (0);
}