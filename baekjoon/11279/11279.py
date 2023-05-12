from sys import stdin
import heapq
n = int(stdin.readline())

heap = []
for i in range(n):
    value = int(stdin.readline())
    if value == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    heapq.heappush(heap, -value)
