import sys 
sys.stdin = open('input2.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            s = arr[i] + arr[j] + arr[k]
            if s <= M:
                if ans < s:
                    ans = s
print(ans)

