import sys
input = sys.stdin.readline


def isWall(r,c,d):
    if d == 0:
        if arr[r+1][c] == 1:
            return True
        return False
    elif d == 1:
        if arr[r][c-1] == 1:
            return True
        return False
    elif d == 2:
        if arr[r-1][c] == 1:
            return True
        return False
    else:
        if arr[r][c+1] == 1:
            return True
        return False
    

def moveBack(r,c,d):
    tmp_row = r
    tmp_col = c
    if d == 0:
        tmp_row += 1
    elif d == 1:
        tmp_col -= 1
    elif d == 2:
        tmp_row -= 1
    else:
        tmp_col += 1

    return tmp_row, tmp_col


def DFS(r,c,d):
    global cnt

    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1

    
    isClean = True
    for i in range(d-1, d-4-1, -1):
        direction = (i+4)%4  # 반시계방향
        row = r + d_row[direction]
        col = c + d_col[direction]
        if row >= 0 and row < N and col >= 0 and col < M:
            if arr[row][col] == 0:
                isClean = False
                DFS(row,col,direction)
                break

    
    if isClean:
        if isWall(r,c,d):
            return
        else:
            move = moveBack(r,c,d)
            move_row = move[0]
            move_col = move[1]
            DFS(move_row, move_col, d)
            
        
        
        


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

d_row = [-1,0,1,0]  # 북, 동, 남, 서
d_col = [0,1,0,-1]

cnt = 0
DFS(r,c,d)
print(cnt)