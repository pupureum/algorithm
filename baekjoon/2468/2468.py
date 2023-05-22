from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
graph = []
max_h = 0
for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    max_h = max(max_h, max(graph[i]))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, m):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == True or graph[nx][ny] <= m:
                continue
            q.append((nx,ny))
            visited[nx][ny] = True

answer = 0
for m in range(max_h):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > m and visited[i][j] == False:
                bfs(i,j,m)
                count += 1
    answer = max(answer, count)
print(answer)
                


