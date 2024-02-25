import sys
input = sys.stdin.readline
import re
from collections import deque

N = int(input())
room = [[] for _ in range(N)]
for i in range(N):
    room[i] = list(input().rstrip())
    

row_cnt = 0
for i in range(N):
    row = room[i]
    cnt = 0
    for j in range(N):
        if row[j] == 'X':
            cnt = 0
        elif row[j] == '.' and cnt >= 2:
            continue
        elif row[j] == '.' and cnt == 1:
            row_cnt += 1
            cnt += 1
        elif row[j] == '.':
            cnt += 1

col_cnt = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == 'X':
            cnt = 0
        elif room[j][i] == '.' and cnt >= 2:
            continue
        elif room[j][i] == '.' and cnt == 1:
            col_cnt += 1
            cnt += 1
        elif room[j][i] == '.':
            cnt += 1
        
    
            
print(row_cnt, col_cnt)
