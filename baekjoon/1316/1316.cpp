#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	int n;
	int k;
	int cnt = 0;
	bool	flag = true;
	string word;
	int temp[26];

	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> word;
		k = 0;
		while(k < 26)
			temp[k++] = 0;
		flag = true;
		for (int j = 0; j < word.size() && flag == true; j++)
		{
			if (temp[word[j] - 'a'] == 0)
			{
				temp[word[j] - 'a'] = 1;
				flag = true;
			}
			else if (temp[word[j] - 'a'] == 1 && word[j-1] != word[j])
				flag = false;
		}
		if (flag == true)
			cnt++;
	}
	cout << cnt;
	return (0);
}