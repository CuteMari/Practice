import sys
input = sys.stdin.readline


N = int(input())
A = [[] for _ in range(N+1)]
for i in range(1,N+1):
    s = input().rstrip()
    for j in range(len(s)):
        if s[j] == 'Y':
            A[i].append(j+1)


M = 0
for i in range(1,N+1):
    visited = [False]*(N+1)
    visited[i] = True
    for j in range(len(A[i])):
        visited[A[i][j]] = True
    
    for j in range(len(A[i])):  # 친구의 친구 연결하기
        sec_idx = A[i][j]
        for k in A[sec_idx]:
            if not visited[k]:
                visited[k] = True
             
    cnt = visited.count(True)-1
    M = max(M, cnt)
print(M)
    



      

