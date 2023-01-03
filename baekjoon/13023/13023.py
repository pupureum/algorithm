'''
    Date : 2022년 12월 12일
    Author : 이푸름
    Description: 백준 ABCDE 13023 문제
'''

import sys

visited = [False] * 2001
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
answer = False

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, depth):
    global answer
    visited[v] = True
    if depth == 4:
        answer = True
        return
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(N):
    dfs(i, 0)
    visited[i] = False
    if answer:
        break
if answer:
    print(1)
else:
    print(0)