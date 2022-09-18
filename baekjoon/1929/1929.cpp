#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
  int min, max;
  cin >> min >> max;
  bool prime[max + 1];
  fill_n(prime, max + 1, true);
  prime[0] = false;
  prime[1] = false;
  
  for (int i = 2; i <= sqrt(max); i++)
  {
    if (prime[i] == true)
      // 기존 수의 n배수를 모두 제거한다.
      // ex) i = 2이면 2*2, 2*3, 2*4, ...는 false
      for (int j = 2 * i; j <= max ; j += i)
        prime[j] = false;
  }
  for (int i = min; i <= max; i++)
  {
    if (prime[i] == true)
      cout << i << '\n';
  }
  return 0;
}

//  endl은 버퍼를 flush하기 때문에 매우 느리다. '\n'을 대신 사용하는 것이 좋다!

/*  소수 빨리 구하는 방법: 에라토스테네스의 체 방식

1. 배열을 만들어서 0과 1을 제외한 수를 true로 초기화한다.
2. max까지 돌면서 소수 아닌 값 false 표시한다.
3. 배열의 크기만큼 for문 돌면서 소수인 값을 출력한다. */