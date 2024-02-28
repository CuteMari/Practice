import sys
input = sys.stdin.readline

def solution(board, moves):
    answer = 0
    B = board
    
    stack = []
    for col in moves:
        for i in range(0, len(B)):
            doll_num = B[i][col-1]
            if doll_num > 0:  # 인형이 존재하면
                B[i][col-1] = 0
                if len(stack) == 0:
                    stack.append(doll_num)
                else:   # 스택에 인형이 존재하면
                    if stack[-1] == doll_num:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(doll_num)
                break


    return answer

if __name__ == '__main__':
    board = [[0,0,0,0,0],  # 2차원 배열
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]  # col단위
    res = solution(board, moves)
    print(res)