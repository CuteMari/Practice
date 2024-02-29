import sys
input = sys.stdin.readline


def solution(N):
        
    DP = [0 for _ in range(N)]
    DP[0] = A[0]
    DP[1] = A[0] + A[1]
    
    for i in range(2, N):
        DP[i] = max(A[i] + A[i-1] + DP[i-3], A[i] + DP[i-2])

    
    return DP[N-1]



if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    
    if N == 1:
        res = A[0]
    elif N == 2:
        res = A[0] + A[1]
    else:
        res = solution(N)

    print(res)