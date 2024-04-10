import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))

total = 0
idx = 0
while True:
    if total == N-1:
        print(idx+1)
        break
    print(idx+1, end=' ')
    cnt = A[idx]
    A[idx] = 0
    if cnt < 0:
        tmp = abs(cnt)
        while tmp > 0:
            idx = (idx - 1 + N)%N
            if A[idx] != 0:
                tmp -= 1
    elif cnt > 0:
        tmp = 0
        while tmp < cnt:
            idx = (idx + 1 + N)%N
            if A[idx] != 0:
                tmp += 1
    total += 1

            
            