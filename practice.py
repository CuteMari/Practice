import sys
input = sys.stdin.readline

def DFS(idx, depth):
    ans.append(A[idx])
    if depth == M-1:
        for i in ans:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            DFS(i, depth+1)
            visited[i] = False
            ans.pop()






N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


for i in range(len(A)):
    visited = [False for _ in range(N)]
    visited[i] = True
    ans = []
    DFS(i, 0)