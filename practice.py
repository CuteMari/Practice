import sys
input = sys.stdin.readline


def solution(string):
    idx = 0
    cnt = 0

    stack = []
    isLaser = True
    for i in range(len(string)):
        c = string[i]
        if c == '(':
            stack.append(c)
            isLaser = True  # 레이저가 될 가능성이 있음
        else:
            if isLaser:
                stack.pop()
                isLaser = False
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    
    return cnt

if __name__ == "__main__":
    stick = input().rstrip()
    res = solution(stick)
    print(res)