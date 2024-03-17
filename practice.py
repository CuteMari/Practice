import sys
input = sys.stdin.readline

def dfs(v, start, height, visited):
    if v != start and len(height[v]) == 0:
        return 1
    
    k = 0
    for i in height[v]:
        if not visited[i]:
            visited[i] = True
            k += dfs(i, start, height, visited)

    if v == start: return k
    return k+1



def solution(taller, smaller):
    answer = 0

    for i in range(1, N+1):
        visited = [False]*(N+1)
        visited[i] = True
        t = dfs(i, i, taller, visited)
        visited = [False]*(N+1)
        visited[i] = True
        s = dfs(i, i, smaller, visited)

        if t+s+1 == N:
            answer += 1

    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    TallerthanMe = [[] for _ in range(N+1)]
    SmallerthanMe = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        TallerthanMe[a].append(b)
        SmallerthanMe[b].append(a)


    res = solution(TallerthanMe, SmallerthanMe)
    print(res)
    