import sys
input = sys.stdin.readline
from collections import deque

def BFS(r,c,color, visited):
    answer = 0
    queue = deque()
    queue.append((r,c))

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    while queue:
        now = queue.pop()
        for i in range(4):
            next_r = now[0] + dr[i]
            next_c = now[1] + dc[i]
            if next_r >= 0 and next_r < m and next_c >= 0 and next_c < n:
                if not visited[next_r][next_c] and picture[next_r][next_c] == color:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))
                    answer += 1

    return answer

def solution(m,n,picture):

    cnt = 0
    maxValue = 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if picture[i][j] != 0 and visited[i][j] == False:
                cnt += 1
                color = picture[i][j]
                tmp = BFS(i,j,color, visited)
                maxValue = max(maxValue, tmp)



    return cnt, maxValue


if __name__ == "__main__":
    m = 6
    n = 4
    picture = [[1, 0, 0, 1 ],[ 1, 0, 0, 1 ],[1, 0, 0, 1 ],[1, 0, 0, 1 ],[1, 0, 0, 1 ],[1,1,1,1]]
    res = solution(m,n,picture)
    print(res[0], res[1])