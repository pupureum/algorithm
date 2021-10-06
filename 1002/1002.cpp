#include <iostream>
using namespace std;

int square(int n)
{
	n = n * n;
	return (n);
}

int cal_answer(int dis, int r1, int r2)
{
	if (dis > square(r1 + r2) || dis < square(r1 - r2))
		return (0);
	else if (dis == square(r2 - r1) || dis == square(r1 + r2))
		return (1);
	else if (dis < square(r1 + r2))
		return (2);
	else
		return (0);
}

int main(void)
{
	int n, x1, y1,r1, x2, y2, r2;

	cin >> n;
	while (n > 0)
	{
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		if (x1 == x2 && y1 == y2 && r1 == r2)
		{
			cout << -1 << endl;
			n--;
			continue;
		}
		cout << cal_answer((square(x1 - x2) + square(y1 - y2)), r1, r2) << endl;
		n--;
	}
	return (0);
}
