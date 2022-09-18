#include <iostream>
#include <cmath>

using namespace std;

int main(void)
{
	double A, B, V;
	int result = 0;

	cin >> A >> B >> V;
	result = 1 + ceil((V - A) / (A - B));
	cout << result << endl;
	return (0);
}