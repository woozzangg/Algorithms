import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    A, B = list(map(int, input().split()))
    arr = [[0]*B for _ in range(A)]
    for i in range(A):
        for j in range(B):
            arr[i][j] = 1+ i*B + j
    # print(*arr)
    for i in arr:
        print(*i)