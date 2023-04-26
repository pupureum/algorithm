import math

n = int(input())
m = int(input())
light_x = list(map(int, input().split()))
last, answer = light_x[0], light_x[0]

for i in range(1, len(light_x)):
    distance = math.ceil((light_x[i] - last) / 2)
    answer = max(answer, distance)
    last = light_x[i]

answer = max(answer, n - light_x.pop())
print(answer)