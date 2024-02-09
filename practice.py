import sys
input = sys.stdin.readline
from queue import PriorityQueue

pq = PriorityQueue()
ans = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if pq.qsize() == 0: 
            print(0)
        else:
            k = pq.get()
            print(k[1])
    else:
        pq.put((-x, x))

