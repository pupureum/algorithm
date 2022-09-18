#include <iostream>
#include <string>
using namespace std;

int	check_croatia(string word, int i)
{
	int len;

	len =  word.size();
	if (i ==len)
		return (1);
	else if (i + 1 <= len &&
		((word[i] == 'c' && (word[i + 1] == '=' || word[i + 1] == '-'))
		|| (word[i] == 'd' && word[i + 1] == '-')
		|| (word[i + 1] == 'j' && (word[i] == 'l' || word[i] == 'n'))
		|| (word[i + 1] == '=' && (word[i] == 's' || word[i] == 'z'))))
		return (2);
	else if (i + 2 <= len &&
		(word[i] == 'd' && word[i + 1] == 'z' && word[i + 2] == '='))
		return (3);
	else
		return(1);
}

int main(void)
{
	string word;
	int num = 0;
	int i = 0;

	cin >> word;
	while(i < word.size())
	{
		i += check_croatia(word, i);
		num++;
	}
	cout << num;
	return (0);
}