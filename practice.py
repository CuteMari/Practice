import sys
input = sys.stdin.readline
from collections import deque
import math

row = [3,0,0,0,1,1,1,2,2,2]  # 0 1,2,3,4,5,6,7,8,9
col = [1,0,1,2,0,1,2,0,1,2]  # 0 1,2,3,4,5,6,7,8,9

def solution(numbers, hand):
    answer = ''
    Left = [1,4,7]
    Right = [3,6,9]
    L_pos = [3,0]   # * 자리 번호
    R_pos = [3,2]   # # 자리 번호


    for i in numbers:
        target_row_pos = row[i]
        target_col_pos = col[i]
        if i in Left:
            answer += 'L'
            L_pos = [target_row_pos,target_col_pos]
        elif i in Right:
            answer += 'R'
            R_pos = [target_row_pos,target_col_pos]
        else:
            L_gap = abs(target_row_pos - L_pos[0]) + abs(target_col_pos - L_pos[1])
            R_gap = abs(target_row_pos - R_pos[0]) + abs(target_col_pos - R_pos[1])
            if L_gap == R_gap:
                if hand == "right": 
                    answer += 'R'
                    R_pos = [target_row_pos,target_col_pos]
                else: 
                    answer += 'L'
                    L_pos = [target_row_pos,target_col_pos]
            elif L_gap > R_gap:
                answer += 'R'
                R_pos = [target_row_pos,target_col_pos]
            else:
                answer += 'L'
                L_pos = [target_row_pos,target_col_pos]

    return answer


if __name__ == "__main__":
    numbers = [0,0]
    hand = "right"
    k = solution(numbers, hand)
    print(k)