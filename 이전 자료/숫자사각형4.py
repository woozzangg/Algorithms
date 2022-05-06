import sys
sys.stdin = open('input_1.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    A = int(input())
    arr = [[0]*A for _ in range(A)]
    # print(arr)
    for i in range(A):
        for j in range(A):
            arr[i][j] = (i+1)*(j+1)
    # # print(*arr)
    for i in arr:
        print(*i)