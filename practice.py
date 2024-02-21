import sys
input = sys.stdin.readline

def solution(s):
    answer = 0

    min = len(s)
    for l in range(1, len(s)+1):
        length = len(s)
        start = 0
        end = l-1    
        while start <= len(s) - 1:
            if end > len(s) - 1:
                tmp = s[start:len(s)-1]
                break
            else:
                tmp = s[start:end+1]
                cnt = 0
                while s[start:end+1] == tmp:
                    cnt += 1
                    start += l
                    end += l
                if cnt > 1:
                    length -= (cnt-1)*(len(tmp))
                    length += len(str(cnt))


        
        if length < min:
            min = length
            
    answer = min

    return answer




if __name__ == "__main__":
    s = input().rstrip()
    answer = solution(s)
    print(answer)



