import sys
input = sys.stdin.readline

def solution(P):
    arr = [0 for _ in range(len(P))]

    for i in range(1,len(P)):
        arr[i] = arr[i-1] + P[i]


    ans = sum(arr)
    return ans


if __name__ == '__main__':
    N = int(input())
    P = [0] + list(map(int, input().split()))   # 1번부터 시작!
    P.sort()
    res = solution(P)
    print(res)