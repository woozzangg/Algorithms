import sys
sys.stdin = open('파리퇴치.txt')

T = int(input())
dx = [1, 1, -1, -1]
dy = [-1,1, -1,  1]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for x in range(N):
        for y in range(N):
            total = arr[x][y]
            for j in range(1,M+1):
                for i in range(4):
                    X, Y = x+dx[i]*j, y+dy[i]*j
                    if 0 <= X < N and 0 <= Y < N:
                        total += arr[X][Y]
            if total >= ans:
                ans = total
    print(f'#{tc} {ans}')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#
#     for x in range(N):
#         for y in range(N):
#             if x == y:
#                 ans += arr[x][y]
#             elif x == (N-y-1):
#                 ans += arr[x][N-y-1]
#     if N % 2 == 1:
#         ans -= arr[N//2][N//2]
#     print(ans)
