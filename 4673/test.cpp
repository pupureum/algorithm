#include <iostream>
using namespace std;

bool arr[10000] = {true};

int is_selfnum(int n){
	int sum;
	
	sum = n;
	while (n != 0)
	{
		sum += n % 10;
		n /= 10;
	}
	return (sum);
}

int main(void)
{
	int num = 0;

	for (int i = 1; i < 10001; i++)
	{
		num = is_selfnum(i);
		if (num <= 10000)
			arr[num] = false;
	}
	for (int j = 1; j < 10000; j++) //배열의 idx가 9999까지니 for문의 범위 주의!!!!!!!!
	{
		if (arr[j] ==  true)
			cout << j << endl;
	}
	return (0);
}