from sys import stdin

n = int(stdin.readline())
answer = [0] * n
values = list(map(int, stdin.readline().split()))

for i in range(1, n + 1):
    value = values[i - 1]
    cnt = 0
    for j in range(n):
        if cnt == value and answer[j] == 0:
            answer[j] = i
            break
        elif answer[j] == 0:
            cnt += 1
print(*answer)