import sys
input = sys.stdin.readline

def calculate(A_idx, op_idx, sum):
    if op_idx == 0:
        sum += A[A_idx]
    elif op_idx == 1:
        sum -= A[A_idx]
    elif op_idx == 2:
        sum *= A[A_idx]
    else:
        sum /= A[A_idx]

    return int(sum)


def dfs(A_idx, op_idx, sum):
    global Min, Max
    sum = calculate(A_idx, op_idx, sum)

    if A_idx == N-1:
        if sum < Min:
            Min = sum
        if sum > Max:
            Max = sum
        return
    for i in range(4):
        if visited[i] > 0:
            visited[i] -= 1
            dfs(A_idx+1, i, sum)
            visited[i] += 1





N = int(input())
A = list(map(int, input().split()))
OP = list(map(int, input().split()))  # +, -, x, /
Min = sys.maxsize
Max = -sys.maxsize


for i in range(4):
    visited = [k for k in OP]
    if visited[i] > 0:
        visited[i] -= 1
        dfs(1, i, A[0])


print(Max)
print(Min)


