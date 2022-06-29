import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(R, cnt):
    visited[R] = True

    ans[R] = cnt

    for i in arr[R]:
        if visited[i] == False:

            dfs(i, cnt+1)


N, M, R = map(int,input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int ,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(N): # 내름차순 정렬
    arr[i+1].sort(reverse=True)
# print(arr)
ans = [-1 for _ in range(N+1)]
# print(ans)

cnt = 0
visited = [False for _ in range(N+1)]
dfs(R, cnt)
for i in range(1,N+1):
    print(ans[i])



# Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어져서 에러가 나는 것입니다.
#
# import sys
#
# sys.setrecursionlimit(n)을 사용하면 재귀의 깊이를 늘릴 수 있습니다.
#
# n에는 원하시는 값을 넣으면 됩니다.