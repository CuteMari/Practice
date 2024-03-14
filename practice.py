import sys
input = sys.stdin.readline
from collections import deque

def solution(board, turninfo):
    answer = 0

    queue = deque()
    nowR = 1
    nowC = 1
    dir_idx = 0
    isEnd = False
    queue.append((1,1))
    for snake in turninfo:
        time = snake[0]
        while answer < time:
            if dir_idx == 0:
                nowC += 1
            elif dir_idx == 1:
                nowR -= 1
            elif dir_idx == 2:
                nowC -= 1
            else:
                nowR += 1
            answer += 1
            
            if nowR < 1 or nowR > N or nowC < 1 or nowC > N or board[nowR][nowC] == 1:
                isEnd = True
                break
            
            if board[nowR][nowC] != 2:
                rear = queue.pop()
                board[rear[0]][rear[1]] = 0
            queue.appendleft((nowR, nowC))
            board[nowR][nowC] = 1



        dir = snake[1]
        if dir == 'L':
            dir_idx += 1
        else:
            dir_idx -= 1
        dir_idx = (dir_idx + 4) % 4
        if isEnd: break

    if isEnd: return answer
    else:
        while True:
            if dir_idx == 0:
                nowC += 1
            elif dir_idx == 1:
                nowR -= 1
            elif dir_idx == 2:
                nowC -= 1
            else:
                nowR += 1
            answer += 1

            if nowR < 1 or nowR > N or nowC < 1 or nowC > N or board[nowR][nowC] == 1:
                    isEnd = True
                    break
                    
            if board[nowR][nowC] != 2:
                rear = queue.pop()
                board[rear[0]][rear[1]] = 0
            queue.appendleft((nowR, nowC))
            board[nowR][nowC] = 1


    return answer


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        board[a][b] = 2
    
    L = int(input())
    turninfo = []
    for _ in range(L):
          info = input().rstrip().split()
          X = int(info[0])
          C = info[1]
          turninfo.append((X,C))


    res = solution(board, turninfo)
    print(res)