import sys
input = sys.stdin.readline


def solution(N):
    answer = 0

    dp = [0 for _ in range(5001)]
    dp[2] = 3

    for i in range(3,5001):
        if i%2 == 1:
            continue
        for j in range(2, i-2+1, 2):
            if j == i-2: dp[i] += dp[2]*dp[j]
            else: dp[i] += 2*dp[j]
        dp[i] += 2

        dp[i] %= 1000000007

    answer = dp[N]


    return answer




if __name__ == "__main__":
    N = int(input())
    res = solution(N)
    print(res)
