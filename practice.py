import sys
input = sys.stdin.readline


def backtrack(r,n,is_queen_in_col, is_queen_in_left, is_queen_in_right):
    if r == n:
        return 1
    

    ret = 0

    for c in range(n):
        if not is_queen_in_col[c] and not is_queen_in_right[r+c] and not is_queen_in_left[n-1+r-c]:
            is_queen_in_col[c] = True
            is_queen_in_right[r+c] = True
            is_queen_in_left[n-1+r-c] = True


            ret += backtrack(r+1, n, is_queen_in_col, is_queen_in_left, is_queen_in_right)


            is_queen_in_col[c] = False
            is_queen_in_right[r+c] = False
            is_queen_in_left[n-1+r-c] = False


    return ret


def solution(n):
    SIZE = 15
    is_queen_in_col = [False]*((SIZE-1)*2)
    is_queen_in_left = [False]*((SIZE-1)*2)
    is_queen_in_right = [False]*((SIZE-1)*2)
    
    answer = backtrack(0,n,is_queen_in_col, is_queen_in_left, is_queen_in_right)

    return answer

if __name__ == "__main__":
    N = int(input())
    ans = solution(N)
    print(ans)