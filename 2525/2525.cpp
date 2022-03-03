#include <iostream>
using namespace std;

int main(void)
{
	int hour, minute, add, total_m;

	cin >> hour >> minute >> add;

	total_m = minute + add;
	if (total_m >= 60)
	{
		hour += total_m / 60;
		total_m %= 60;
	}
	if (hour > 23)
		hour -= 24;
	cout << hour << " " << total_m << std::endl;
	return (0);
}