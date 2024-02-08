import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
myList = [[] for _ in range(V+1)]
distance = [sys.maxsize]*(V+1)
visited = [False]*(V+1)
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    myList[u].append((v,w))

q.put((0,K))
distance[K] = 0

while q.qsize() > 0:
    now = (q.get())[1]
    if visited[now]: continue
    visited[now] = True

    for tmp in myList[now]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[now] + value:
            distance[next] = distance[now] + value
            q.put((distance[next], next))
        

for i in range(1,V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")