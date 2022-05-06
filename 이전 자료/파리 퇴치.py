import sys
sys.stdin = open('파리퇴치.txt')
#
# T = int(input())
#
# def kill_area(index):
#     sum_a = 0
#     for j in range(index):
#         for i in range(index):
#             sum_a += matrix[row+i][col+j]
#     return sum_a
#
#
#
# for tc in range(1,T+1):
#     N, M = list(map(int, input().split()))
#     max_kill = 0
#     matrix = [list(map(int,input().split())) for _ in range(N)]
#     for col in range(N-M+1):
#         for row in range(N-M+1):
#             if kill_area(M) >= max_kill:
#                 max_kill = kill_area(M)
#     print(f'#{tc} {max_kill}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 모든 사각영역의 좌상단 시작점 좌표 (x, y)
    for x in range(N-M+1):
        for y in range(N-M+1):
            total = 0
            # 파리채
            for i in range(M):
                for j in range(M):
                    total += arr[x+i][y+j]
            if ans < total:
                ans = total
    print(f'#{tc} {ans}')