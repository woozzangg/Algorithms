import sys
sys.stdin = open('구구단1.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    A, B = list(map(int, input().split()))
    # if A <= B:
    #     for j in range(1, 10):
    #         for i in range(A, B + 1):
    #             print(f'{i} * {j} = {i * j}')
    #
    # elif A > B:
    #     for j in range(1, 10):
    #         for i in range(A, B - 1, -1):
    #             print(f'{i} * {j} = {i * j}')

    #-------------------------------------------------------
    # if A <= B:
    #     for j in range(1, 10):
    #         for i in range(A, B + 1):
    #             print(f'{i} * {j} = {i * j}', end='   ')
    #         print('')
    # elif A > B:
    #     for j in range(1, 10):
    #         for i in range(A, B - 1, -1):
    #             print(f'{i} * {j} = {i * j}', end='   ')
    #         print('')
            #-------------------------------


    if A <= B:
        for j in range(1, 10):
            for i in range(A, B + 1):
                # print('%d * %d = %2d' % (i, j, i*j),end='   ')
                print(f'{i} * {j} = {i * j:2d}', end='   ')
            print('')
    elif A > B:
        for j in range(1, 10):
            for i in range(A, B - 1, -1):
                # print('%d * %d = %2d' % (i, j, i * j), end='   ')
                print(f'{i} * {j} = {i * j:2d}', end='   ')
            print('')

    #---------------------------------
    (f'#{tc} {tastrdaf}')




    #-------------------------------------------------------
    # if A <= B:
    #     for j in range(1, 10):
    #         print(f'{i} * {j} = {i * j}', sep='   ', for i in range(A, B+1))
    # elif A > B:
    #     for j in range(1, 10):
    #
    #         print(f'{i} * {j} = {i * j}', sep='   ',for i in range(A, B - 1, -1))

