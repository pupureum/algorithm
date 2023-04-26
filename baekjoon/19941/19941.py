n, k = map(int, input().split())
position = list(input())
answer = 0 

for i in range(n):
    if position[i] == 'P':
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if position[j] == 'H':
                position[j] = 'D'
                answer += 1
                break
print(answer)