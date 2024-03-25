import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = [[] for _ in range(K)]
idx = 0
for i in range(0, N, N//K):
    tmp = A[i:i+N//K]
    tmp.sort()
    ans[idx] = tmp
    idx += 1

for k in ans:
    for j in k:
        print(j, end=' ')

