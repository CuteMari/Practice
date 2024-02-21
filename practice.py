import sys
input = sys.stdin.readline
from queue import PriorityQueue
import heapq

def solution(N):
    answer = 0
       
    pq = PriorityQueue()
    for i in range(N):
        S,T = map(int, input().split())
        pq.put((S,T))
        
    
    room = [0]
    while pq.qsize() > 0:
        lecture = pq.get()
        lecture_start = lecture[0]
        lecture_end = lecture[1]

        if lecture_start >= room[0]:
            heapq.heappop(room)
            heapq.heappush(room, lecture_end)
        else:
            heapq.heappush(room, lecture_end)

    answer = len(room)
   
  
    return answer




if __name__ == "__main__":
    N = int(input())
    res = solution(N)
    print(res)

