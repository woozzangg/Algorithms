import sys
sys.stdin = open('농작물 수확하기.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    start = end = mid = N // 2 # N =7  , mid = 3
    total = 0
    for i in range(N, -1, -1):
        for j in range(start, end+1):
            total += arr[i][j]

        if i < mid:
            start -= 1 # 3   2  1 0
            end += 1   # 3   4  5 6
        else:
            start += 1
            end -= 1

    print(f'#{tc} {total}')
