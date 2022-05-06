import sys
sys.stdin = open('input_2.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    N, M = list(map(int, input().split()))
    if M == 1:
        for i in range(1, N+1):
            print('*'*i)
    elif M == 2:
        for i in range(N,0,-1):
            print('*'*i)
    else:
        for i in range(1, N+1):
            print('{:^20}'.format('*'*(2*i-1)))

        # for i in range(1,N+1):
        #     print('*'*(2*i-1))
        # arr = [[''] * (2*N -1) for _ in range(N)]
        # print(arr)
        # for i in range(N):
        #     for j in range(N):
        #         arr[i][j] = 1 + i * N + j
        # # print(*arr)
        # for i in arr:
        #     print(*i, end='')

