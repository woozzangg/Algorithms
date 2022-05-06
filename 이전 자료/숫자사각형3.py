# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     print(f'#{tc}')
#     A, B = list(map(int, input().split()))
#     arr = [[0]*B for _ in range(A)]
#     for i in range(A):
#         for j in range(B):
#             arr[i][j] = 1+ i*B + j
#             N = i
#             if N % 2 == 1:
#                 arr[i][j] = 1+ i*B + ((B-1)-j)
#     # print(*arr)
#     for i in arr:
#         print(*i)
#
#
#
#

import sys
sys.stdin = open('숫자사각형1.txt')

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [[0]* W for _ in range(H)]

    num = 1
    for i in range(W):
        for j in range(H):
            arr[j][i] = num
            num += 1



    print(f'#{tc}')
    for i in range(H):
        for j in range(W):
            print(arr[i][j], end=' ')
        print()
arr = [ [0]*n for _ in range N]