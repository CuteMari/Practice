import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    queue = deque()
    queue.append((i,j, 1))
    
    drow = [1,0,-1,0]
    dcol = [0,1,0,-1]
    ans = 0
    while queue:
        now = queue.popleft()
        if now[0] == N-1 and now[1] == M-1:
            ans = now[2]
            break
        for i in range(4):
            row = now[0] + drow[i]
            col = now[1] + dcol[i]
            cnt = now[2]
            if row >= 0 and row < N and col >= 0 and col < M and maze[row][col] == 1:
                if not visited[row][col]:
                    visited[row][col] = True
                    queue.append((row, col, cnt+1))

    print(ans)

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))


visited = [[False for _ in range(M)] for _ in range(N)]

bfs(0,0)