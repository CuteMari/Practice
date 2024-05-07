import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

buckets = [deque() for _ in range(10)]

max_val = max(A)
queue = deque(A)
digit = 1

while max_val >= digit:
    while queue:
        num = queue.popleft()
        buckets[(num // digit) % 10].append(num)
    
    for bucket in buckets:
        while bucket:
            queue.append(bucket.popleft())
    digit *= 10


while queue:
    print(queue.popleft())