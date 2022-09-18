#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
	string str1, str2;
	vector<int> A, B, sum;

	cin >> str1 >> str2;
	if (str1.size() < str2.size()) //긴 숫자를 str1에
		swap(str1, str2);
	
	int dif = str1.size() - str2.size(); //더 짧은 숫자 str2 앞부분에는 0으로 채우기
	for (int i = 0; i < str1.size(); i++)
	{
		A.push_back(str1[i] - '0');
		if (i < dif)
			B.push_back(0);
		else
			B.push_back(str2[i - dif] - '0');
	}

	bool isCarry = false; //반올림 변수
	for (int i = str1.size() - 1; i >= 0; i--)
	{
		int temp;
		if (isCarry)
			temp = A[i] + B[i] + 1;
		else
			temp = A[i] + B[i];
		if (temp >= 10)
		{
			isCarry = true;
			temp -= 10;
		}
		else
			isCarry = false;
		sum.push_back(temp);
	}
	if (isCarry)
		sum.push_back(1); //마지막에 반올림이 있는경우

	for (int i = sum.size() - 1; i >= 0; i--) //뒤에서부터 더하여 벡터에 저장하므로 역순으로 저장되어 있음
		cout << sum[i];
	return (0);
}