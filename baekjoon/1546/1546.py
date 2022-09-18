n = int(input())
score = list(map(int, input().split()))
max = max(score)

for i in range(n):
    score[i] = score[i] / max * 100
avg = sum(score) / n
print(round(avg,3))