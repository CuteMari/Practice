import sys
input = sys.stdin.readline


def floydWarshall(A):
    for k in range(1,N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])


def calcDistance(roomNum, A, P):
    distance = 0
    for i in P:
        distance += A[i][roomNum]

    return distance


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        arr[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a][b] = c
        arr[b][a] = c

    floydWarshall(arr)


    K = int(input())
    roomP = list(map(int, input().split()))
    minValue = sys.maxsize 
    minNum = 0
    for i in range(1,N+1):
        if minValue > calcDistance(i, arr, roomP):
            minValue = calcDistance(i, arr, roomP)
            minNum = i

    print(minNum)