import sys
input = sys.stdin.readline
from collections import deque

S = input().rstrip()
stack = []
queue = deque()

for i in range(len(S)):
    queue.append(S[i])


isTag = False
while queue:
    now = queue.popleft()
    if now == '<':
        while len(stack) > 0:
            print(stack.pop(), end='')
        isTag = True
        print(now, end='')
    elif now == '>':
        isTag = False
        print(now, end='')
    elif now == ' ':
        while len(stack) > 0:
            print(stack.pop(), end='')
        print(now, end='')
    else:
        if isTag:
            print(now, end='')
        else:
            stack.append(now)

while len(stack) > 0:
    print(stack.pop(), end='')