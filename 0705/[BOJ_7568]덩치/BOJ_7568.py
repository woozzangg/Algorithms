import sys 
sys.stdin = open('input1.txt') 

N = int(input())
ans = [1 for _ in range(N)]
arr = []
for i in range(N):
    t = list(map(int,input().split()))
    arr.append(t)

for i in range(N):
    for j in range(N):
        if i == j:
            pass
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            ans[i] += 1
for i in range(N):
    print(ans[i], end=' ')