import sys 
sys.stdin = open('input1.txt') 

N = int(input())

result = 0
for i in range(1,N+1):
    A = list(map(int, str(i)))
    result = i + sum(A)
    if result == N:
        print(i)
        break
    if i == N:
        print(0)

import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []


for _ in range(n):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")
    else:
        heapq.heappush(heap, [-num, num])