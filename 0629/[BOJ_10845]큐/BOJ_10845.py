import sys
sys.stdin = open('input1.txt')
from collections import deque
input = sys.stdin.readline
N = int(input())
q = deque()
for i in range(N):
    arr = input()
    # print(arr[:2])
    # print(arr[5:])
    if arr[:2] == 'pu':
        q.append(arr[5])
    elif arr[:2] == 'po':
        if q:
            n=q.popleft()
            print(n)
        else:
            print('-1')
    elif arr[:2] == 'si':
        print(len(q))
    elif arr[:2] == 'em':
        if q:
            print('0')
        else:
            print('1')
    elif arr[:2] == 'fr':
        if q:
            print(q[0])
        else:
            print('-1')
    elif arr[:2] == 'ba':
        if q:
            print(q[-1])
        else:
            print('-1')
#
# import sys
#
# N = int(sys.stdin.readline())
#
# queue = []
#
# for i in range(N):
#     cmd = sys.stdin.readline().split()
#
#     if cmd[0] == "push":
#         queue.insert(0, cmd[1])
#         ##print(queue)
#
#     elif cmd[0] == "pop":
#         if len(queue) != 0: print(queue.pop())
#         else: print(-1)
#
#     elif cmd[0] == "size":
#         print(len(queue))
#
#     elif cmd[0] == "empty":
#         if len(queue) == 0: print(1)
#         else : print(0)
#
#     elif cmd[0] == "front":
#         if len(queue) == 0: print(-1)
#         else: print(queue[len(queue) -1])
#
#     elif cmd[0] == "back":
#         if len(queue) == 0: print(-1)
#         else: print(queue[0])