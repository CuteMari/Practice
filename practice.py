import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()
ans = 0
weight = []
for _ in range(N):
    l = int(input())
    pq.put(l)

while pq.qsize() > 0:
    w = pq.get()
    ans = max(ans, w, w*(pq.qsize()+1))

print(ans)