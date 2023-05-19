from sys import stdin
from collections import deque

num = int(stdin.readline().rstrip())
pair = int(stdin.readline().rstrip())
graph = [[] for _ in range(num + 1)]
for i in range(pair):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (num + 1)

def bfs(x):
    q = deque([x])
    visited[1] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)
    print(sum(visited) - 1)

bfs(1)