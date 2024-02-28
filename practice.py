import sys
input = sys.stdin.readline

def solution(s):
    alp = [0 for _ in range(26)]

    isGroup = True
    checkchar = ''
    for i in s:
        if i == checkchar:
            continue
        else:
            if alp[ord(i)-97] == 1:
                isGroup = False
                break
            else:
                alp[ord(i)-97] = 1
                checkchar = i


    return isGroup


if __name__ == '__main__':
    N = int(input())
    cnt = 0
    for _ in range(N):
        s = input().rstrip()
        res = solution(s)
        if res:
            cnt += 1

    print(cnt)