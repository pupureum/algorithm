n = int(input())

for i in range(n):
    r, str = input().split()
    for j in str:
        print(j*int(r), end="")
    print() //줄바꿈
