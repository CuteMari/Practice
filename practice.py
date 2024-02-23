import sys
input = sys.stdin.readline


def dfs(v, depth):
    ans.append(v)
    if depth == M:
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
        return
    for i in range(v, N+1):
        visited[i] = True
        dfs(i, depth+1)
        visited[i] = False
        ans.pop()

N, M = map(int, input().split())


for i in range(1,N+1):
    ans = []
    visited = [False for _ in range(N+1)]
    visited[i] = True
    dfs(i,1)

