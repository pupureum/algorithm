#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string num1;
	string num2;
	string result;

	cin >> num1 >> num2;
	for(int i = 2; i >= 0; i--)
	{
		if (num1[i] == num2[i])
			continue;
		if(num1[i] > num2[i])
			result = num1;
		else
			result = num2;
		break;
	}	
	cout << result[2] << result[1] << result[0];
	return (0);
}