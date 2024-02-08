import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
D = [sys.maxsize]*(N+1)
visited = [False]*(N+1)
q = PriorityQueue()

for _ in range(M):
    u, v, w = map(int, input().split())
    bus[u].append((v,w))

startDosi, endDosi = map(int, input().split())
D[startDosi] = 0
q.put((0, startDosi))


while q.qsize() > 0:
    now = (q.get())[1]
    if visited[now]:
        continue
    visited[now] = True
    for tmp in bus[now]:
        next = tmp[0]
        value = tmp[1]
        if D[next] > D[now] + value:
            D[next] = D[now] + value
            q.put((D[next], next))


print(D[endDosi])