#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string word;
	int div = 0, result = 0;

	cin >> word;
	for (int i = 0; i < word.size(); i++)
	{
		if (word[i] < 'S')
			div = (word[i] - 'A') / 3;
		else if (word[i] >= 'S' && word[i] < 'Z')
			div = (word[i] - 'A' - 1) / 3;
		else
			div = 7;
		result += (div + 3);
	}
	cout << result << endl;

	return (0);
}