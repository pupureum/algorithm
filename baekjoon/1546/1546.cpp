#include <iostream>
using namespace std;

double get_sum(int max, double* score, int n)
{
    double sum = 0;

    for (int j = 0; j < n; j++)
    {
        score[j] = score[j] / max * 100;
        sum += score[j];
    }
    return (sum / n);
}

int main(void)
{
    int n;
    double score[1000] = {}, avg = 0, max = 0;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> score[i];
        if (max < score[i])
            max = score[i];
    }
    avg = get_sum(max, score, n);
    cout << fixed;
    cout.precision(3);
    cout << avg << endl;
    return (0);
}