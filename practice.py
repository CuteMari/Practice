import sys
input = sys.stdin.readline



cnt = 0
N, P = map(int, input().split())
finger = [[] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    while len(finger[a]) > 0 and finger[a][-1] > b:
        finger[a].pop()
        cnt += 1
    if len(finger[a]) > 0 and finger[a][-1] == b:
        continue
    finger[a].append(b)
    cnt += 1

    
print(cnt)
        

