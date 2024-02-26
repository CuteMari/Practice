import sys
input = sys.stdin.readline


def DFS(v, i):
    visited[v] = True   
    next = A[v]
    if not visited[next]:
        DFS(next, i)
    elif visited[next] and next == i:
        result.append(next)

    


N = int(input())
A = [0 for _ in range(N+1)]

for i in range(1,N+1):
    A[i] = int(input())


cnt = 0
result = []
for i in range(1,N+1):
    visited = [False]*(N+1)
    DFS(i,i)


print(len(result))
result.sort()
for i in result:
    print(i)