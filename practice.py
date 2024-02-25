import sys
input = sys.stdin.readline
from collections import deque

def DFS(depth):
    if depth == M:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return
    for i in range(N):
        ans.append(A[i])
        DFS(depth+1)
        ans.pop()
    


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(N):
    ans = []
    ans.append(A[i])
    DFS(1)