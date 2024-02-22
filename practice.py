import sys
input = sys.stdin.readline

def solution(depth, start, cost, graph, visited):
    global M
    if depth == len(visited)-1 and graph[start][0] != 0:
        M = min(M, cost+graph[start][0])
        return
    for i in range(N):
        if not visited[i] and graph[start][i] != 0:
            visited[i] = True
            solution(depth+1, i, cost+graph[start][i], graph, visited)
            visited[i] = False



if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*(N)
    visited[0] = True
    M = sys.maxsize

    solution(0,0,0,graph,visited)

    print(M)