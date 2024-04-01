import sys
input = sys.stdin.readline
import math

Prime = [True]*(10000000)
for i in range(2, int(math.sqrt(10000000))+1):
    if Prime[i]:
        for j in range(i*2, 10000000, i):
            Prime[j] = False


primeList = []
for i in range(2,10000000):
    if Prime[i]:
        primeList.append(i)


T = int(input())
for t in range(T):
    M = int(input())
    A = list(map(int, input().split()))
    checkdic = {}
    for l in A:
        tmp = 0
        for i in range(l):
            tmp += primeList[i]
        checkdic[tmp] = 1
        for i in range(l, len(primeList)):
            j = i - l
            tmp -= primeList[j]
            tmp += primeList[i]
            if tmp >= 10000000: break
            
            if tmp in checkdic:
                checkdic[tmp] += 1
            else:
                checkdic[tmp] = 1
        
    
    print("Scenario " + str(t+1) + ":")
    
    for i in checkdic.keys():
        if Prime[i] and checkdic[i] == M:
            print(i)
            break
    
    print()


