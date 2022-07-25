import sys 
sys.stdin = open('input1.txt') 
from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    s_ = [0 for i in range(n)]
    s_[m] = 1
    cnt = 0
    while True:
        if s[0] == max(s):
            cnt += 1
            if s_[0] == 1:
                print(cnt)
                break
            else:
                del s[0]
                del s_[0]
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]

# T = int(input())
#
# for tc in range(T):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     im = arr[M]
#     impor = deque()
#     for i in range(N):
#         if i == M:
#             impor.append(1)
#         else:
#             impor.append(0)
#     impor[M] = 1
#     q = deque()
#     cnt = 0
#     arr.sort(reverse=True)
#
#     for i in arr:
#         q.append(i)
#     if N == 1:
#         print(1)
#     else:
#         while True:
#             if impor[0] == im:
#                 if arr[0] > im:
#                     n = q.popleft()
#                     q.append(n)
#                     t = impor.popleft()
#                     impor.append(t)
#                 else:







            #
            # if impor[0] == 1:
            #     cntt = 0
            #     for i in q:
            #         if i > im:
            #             cntt += 1
            #     if cntt > 0:
            #         n = q.popleft()
            #         q.append(n)
            #         t = impor.popleft()
            #         impor.append(t)
            #
            #     else:
            #         print(cnt)
            #         break
            # else:
            #     if q[0] >= im:
            #         if cnt > 1:
            #
            #             cnt += 1
            #             q.popleft()
            #             t = impor.popleft()
            #             impor.append(t)
            #         else:
            #             n = q.popleft()
            #             q.append(n)
            #             t = impor.popleft()
            #             impor.append(t)
            #
            #
            #     else:
            #         n=q.popleft()
            #         q.append(n)
            #         t = impor.popleft()
            #         impor.append(t)



