#include <iostream>
 using namespace std;

 int main(void)
 {
	int num, H, W, N, i = 0;

	cin >> num;
	 
	while(i < num)
	{
		cin >> H >> W >> N;

		if (N % H == 0)
			cout << H * 100 + (N / H) <<  endl;
		else
			cout << (N % H) * 100 + (N / H) + 1 << endl;
		i++;
	}
}