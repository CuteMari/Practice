import sys
input = sys.stdin.readline
from collections import deque

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    cnt = 1
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and x < N and y >= 0 and y < N:
                if not visited[x][y] and APT[x][y] == '1':
                    queue.append((x,y))
                    visited[x][y] = True
                    cnt += 1
                
    return cnt




N = int(input())
APT = []
for i in range(N):
    APT.append(list(input().rstrip()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False for j in range(N)] for i in range(N)]

apt_cnt = 0
danzi_cnt = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and APT[i][j] == '1':
            apt_cnt += 1
            res = BFS(i,j)
            danzi_cnt.append(res)

print(apt_cnt)
danzi_cnt.sort()
for i in range(len(danzi_cnt)):
    print(danzi_cnt[i])
