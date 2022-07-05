import sys 
sys.stdin = open('input1.txt') 
# from collections import deque
# input = sys.stdin.readline

N = int(input())
# q = deque()
q = []
for i in range(N):
    a = int(input())
    if a == 0:
        q.pop()
    else:
        q.append(a)
print(sum(q))