import sys
input = sys.stdin.readline

def RowCount(arr):
    cnt = 0

    for i in range(N):
        isContinuous = False
        for j in range(M):
            if arr[i][j] != '-':
                isContinuous = False
            else:
                if not isContinuous:
                    cnt += 1
                    isContinuous = True

    return cnt


def ColCount(arr):
    cnt = 0

    for i in range(M):
        isContinuous = False
        for j in range(N):
            if arr[j][i] != '|':
                isContinuous = False
            else:
                if not isContinuous:
                    cnt += 1
                    isContinuous = True
    
    return cnt

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))


row = RowCount(arr)
col = ColCount(arr)
print(row + col)