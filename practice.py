import sys
input = sys.stdin.readline
from collections import deque

def solution(idx, depth):
    ans.append(A[idx])

    if depth == M:
        result = " ".join(ans)
        if result not in dic:
            dic[result] = 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            solution(i, depth+1)
            ans.pop()
            visited[i] = False



if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = list(map(str, A))
    dic = {}
    for i in range(N):
        visited = [False for _ in range(N)]
        visited[i] = True
        ans = []
        solution(i, 1)

    for i in dic:
        print(i)