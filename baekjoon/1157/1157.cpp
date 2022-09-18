#include <iostream>
#include <string>
#include <vector>
using namespace std;

char	get_result(vector<int> alpha)
{
	int	max = 0, idx = 0;
	bool	signal;

	for (int i = 0; i < alpha.size(); i++)
	{
		if (alpha[i] > max)
		{
			max = alpha[i];
			idx = i;
			signal = false;
		}
		else if (alpha[i] == max && max > 0)
			signal = true;
	}
	if (signal == true)
		return ('?');
	else
		return ('A' + idx);
}

int	main(void)
{
	string	words;
	vector<int>	alpha(26);

	cin >> words;
	for (int i = 0; i < words.size(); i++)
	{
		if (words[i] >= 'a' && words[i] <= 'z')
			alpha[words[i] - 'a']++;
		else if (words[i] >= 'A' && words[i] <= 'Z')
			alpha[words[i] - 'A']++;
		else
			return (-1);
	}
	cout << get_result(alpha) << endl;
	return (0);
}