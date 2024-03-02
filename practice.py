import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
arr = []
arr.append([0 for _ in range(N+1)])
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))


D = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + arr[i][j]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1]
    print(res) 
    