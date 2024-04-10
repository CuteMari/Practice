import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
buffer = deque()

while True:
    x = int(input())
    if x == 0:
        buffer.popleft()
    elif x == -1:
        break
    else:
        if len(buffer) == N:
            continue
        buffer.append(x)
    
    
if not buffer:
    print("empty")
else:
    while buffer:
        print(buffer.popleft(), end=' ')