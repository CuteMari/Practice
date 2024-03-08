import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    log = input().rstrip()
    front = []
    back = []
    cursor = 0

    for c in log:
        if c == '-':
            if front:
                front.pop()
        elif c == '<':
            if front:
                back.append(front.pop())
        elif c == '>':
            if back:
                front.append(back.pop())
        else:
            front.append(c)

       
    print("".join(front) + "".join(back[::-1]))