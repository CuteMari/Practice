import sys
input = sys.stdin.readline

def dfs(v, depth):
    visited[v] = True
    ans.append(v)
    if depth == M:
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
        return
    for i in range(v+1, N+1):
        if not visited[i]:
            visited[i] = True
            dfs(i, depth+1)
            visited[i] = False
            ans.pop()



N, M = map(int, input().split())
for i in range(1,N+1):
    visited = [False for _ in range(N+1)]
    ans = []
    dfs(i, 1)
