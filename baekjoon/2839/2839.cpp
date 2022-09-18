#include <iostream>
using namespace std;

int main(void)
{
	int N, cnt = 0;
	cin >> N;

	while(N > 0)
	{
		if (N % 5 == 0)
		{
			N -= 5;
			cnt++;
		}
		else if (N % 3 == 0)
		{
			N -= 3;
			cnt++;
		}
		else if (N > 5)
		{
			N -= 5;
			cnt++;
		}
		else
		{
			cnt = -1;
			break;
		}
	}
	cout << cnt << endl;
	return (0);
}