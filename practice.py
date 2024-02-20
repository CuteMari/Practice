import sys
input = sys.stdin.readline
from collections import deque

ALP = [0 for _ in range(26)]
name = input().rstrip()

for i in range(len(name)):
    ALP[ord(name[i]) - 65] += 1



left_queue = deque()
right_queue = deque()
for i in range(26):
    cnt = ALP[i]//2
    for j in range(cnt):
        left_queue.append(chr(i+65))
        right_queue.append(chr(i+65))
    

isOddExist = False
isPalin = True
for i in range(26):
    rest = ALP[i]%2
    if rest == 1:
        if isOddExist:  # 홀수개인 알파벳이 존재하면 팰린드롬 불가능
            isPalin = False
            break
        isOddExist = True
        left_queue.append(chr(i+65))


if isPalin:
    while left_queue:
        print(left_queue.popleft(), end='')
    while right_queue:
        print(right_queue.pop(), end='')
else:
    print("I'm Sorry Hansoo")