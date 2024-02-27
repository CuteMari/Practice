import sys
input = sys.stdin.readline
from collections import deque

def Importance(D_cnt, k):
    for i in range(9, k, -1):
        if D_cnt[i] > 0:    # 높은 중요도가 존재하면 False
            return False

    return True  # 높은 중요도가 없으면 True



T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    D = [0] + list(map(int, input().split()))  
    D_cnt = [0] * 10     # 중요도 cnt

    for i in range(1,N+1):
        D_cnt[D[i]] += 1

    queue  = deque()
    for i in range(1,N+1):   # 초기 큐 1(A) ~ Z(26) 저장
        queue.append(i)

    res = 0
    target = M+1
    while queue:  # 중요도 1 ~ 9
        now = queue.popleft()
        isPop = Importance(D_cnt, D[now])
        if isPop:
            res += 1
            D_cnt[D[now]] -= 1
            if now == target:
                print(res)
                break
        else:
            queue.append(now)



