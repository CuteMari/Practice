import sys
input = sys.stdin.readline

N = int(input())
stack = [0] + list(map(int, input().split()))
stack_rest = []
D = [-1 for i in range(N+1)]  # 인덱스 값으로 저장


idx = len(stack) - 1
while idx > 1:
    tmp = idx - 1
    if stack[idx] <= stack[idx - 1]:
        D[idx] = idx - 1
        while len(stack_rest) > 0:
            now_rest_idx = stack_rest.pop()
            if stack[now_rest_idx] <= stack[idx - 1]:
                D[now_rest_idx] = idx - 1
            else:
                stack_rest.append(now_rest_idx)
                break
    else:
        stack_rest.append(idx)
    
    idx -= 1
    
    

while len(stack_rest) > 0:
    D[stack_rest.pop()] = 0

D[1] = 0
for i in range(1,N+1):
    print(D[i], end=' ')
