from sys import stdin

n = int(stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().rstrip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False    

answer = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            answer.append(count)
            count = 0
print(len(answer))
answer.sort()
for a in answer:
    print(a)