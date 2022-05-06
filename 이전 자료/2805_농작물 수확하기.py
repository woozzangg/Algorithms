import sys
sys.stdin = open('농작물 수확하기.txt')




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)

    middle = N // 2
    # for i in range(N):
    #     for j in range(N):
    #         if i < middle:
    #             for k in range(middle):
    #                 arr[middle-k][j]
    #         if i >= middle:
    for i in range(N):
        if i < middle:
            for j in range(N):
                if j < middle-i or j > middle +i:
                    arr[i][j] = 0
        if i > middle:
            for j in range(N):
                if j < i-middle or j > N-(i-middle)-1:
                    arr[i][j] = 0
    arr_sum = 0
    for i in range(N):
        for j in range(N):
            arr_sum += arr[i][j]
    print(f'#{tc} {arr_sum}')