#include <iostream>
#include <string>
using namespace std;

int	main(void)
{
	string s;
	int	cnt = 0;
	bool	word = false;

	getline(cin, s);
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] != ' ' && word == false)
		{
			word = true;
			cnt++;
		}
		else if (s[i] == ' ' && word == true)
			word = false;
	}
	cout << cnt;
	return (0);
}